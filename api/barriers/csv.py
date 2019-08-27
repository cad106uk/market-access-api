import csv
from codecs import BOM_UTF8
from csv import DictWriter
from datetime import datetime
from decimal import Decimal

from django.http import StreamingHttpResponse

from api.core.utils import EchoUTF8

CSV_CONTENT_TYPE = 'text/csv; charset=utf-8'
INCOMPLETE_CSV_MESSAGE = (
    '\r\n'
    'An error occurred while generating the CSV file. The file is incomplete.'
    '\r\n'
).encode('utf-8')


def csv_iterator(rows, field_titles):
    """Returns an iterator producing CSV formatted data from provided input."""
    try:
        yield BOM_UTF8
        writer = DictWriter(
            EchoUTF8(),
            fieldnames=field_titles.keys(),
            quoting=csv.QUOTE_MINIMAL
        )

        yield writer.writerow(field_titles)
        for row in rows:
            yield writer.writerow(_transform_csv_row(row))
    except Exception:
        # Because CSV responses are normally streamed, a 200 response will already have been
        # returned if an error occurs at this point. Hence we append an error to the CSV
        # contents (while re-raising the exception).
        yield INCOMPLETE_CSV_MESSAGE
        raise


def create_csv_response(rows, field_titles, filename):
    """Creates a CSV HTTP response."""
    # Note: FileResponse is not used as it is designed for file-like objects, while we are using
    # a generator here.
    response = StreamingHttpResponse(
        csv_iterator(rows, field_titles),
        content_type=CSV_CONTENT_TYPE,
    )

    response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'
    return response


def _transform_csv_row(row):
    return {key: _transform_csv_value(val) for key, val in row.items()}


def _transform_csv_value(value):
    """
    Transforms values before they are written to a CSV file for better compatibility with Excel.

    In particular, datetimes are formatted in a way that results in better compatibility with
    Excel. Lists are converted to comma separated strings. Other values are passed through 
    unchanged (the csv module automatically formats None as an empty string).

    These transformations are specific to CSV files and won't necessarily apply to other file
    formats.
    """
    if isinstance(value, datetime):
        return value.strftime('%Y-%m-%d')
    if isinstance(value, Decimal):
        normalized_value = value.normalize()
        return f'{normalized_value:f}'
    if isinstance(value, list):
        return "; ".join(str(x) for x in value)
    return value