import operator

from django.db import models

from api.core.validate_utils import DataCombiner

REPORT_CONDITIONS = [
    {
        "stage": "1.1",
        "order": 1,
        "required": ["problem_status", "is_resolved"],
        "conditional": [
            {
                "condition_field": "is_resolved",
                "operator": operator.eq,
                "value": True,
                "non_null_field": "resolved_date",
                "error_message": "resolved_date can not be null, when is_resolved is True",
            }
        ],
    },
    {"stage": "1.2", "order": 2, "required": ["export_country"], "conditional": []},
    {
        "stage": "1.3",
        "order": 3,
        "required": ["sectors_affected"],
        "conditional": []
    },
    {
        "stage": "1.4",
        "order": 4,
        "required": ["product", "source", "barrier_title", "eu_exit_related"],
        "conditional": [
            {
                "condition_field": "source",
                "operator": operator.eq,
                "value": "OTHER",
                "non_null_field": "other_source",
                "error_message": "other_source can not be null, when source is True",
            }
        ],
    },
    {
        "stage": "1.5",
        "order": 5,
        "required": ["problem_description"],
        "conditional": [
            {
                "condition_field": "is_resolved",
                "operator": operator.eq,
                "value": True,
                "non_null_field": "status_summary",
                "error_message": "status_summary can not be null, when is_resolved is True",
            }
        ],
    },
]


def required_field_value(instance, field_name):
    data_combiner = DataCombiner(instance, None)
    meta = instance._meta
    field = meta.get_field(field_name)

    if isinstance(field, models.ManyToManyField):
        value = data_combiner.get_value_to_many(field_name)
    else:
        value = data_combiner.get_value(field_name)

    if value is None:
        return False

    return True


def conditional_field_value(instance, rule_item):
    data_combiner = DataCombiner(instance, None)

    condition_value = data_combiner.get_value(rule_item["condition_field"])
    non_null_value = data_combiner.get_value(rule_item["non_null_field"])
    relate = rule_item["operator"]
    value_to_check = rule_item["value"]
    if condition_value and relate(condition_value, value_to_check):
        if non_null_value is None:
            return False

        return True


def report_stage_status(instance, stage_condition):
    status = []
    for field in stage_condition["required"]:
        status.append(required_field_value(instance, field))

    for item in stage_condition["conditional"]:
        status.append(conditional_field_value(instance, item))

    if True in set(status) and False in set(status):
        return (stage_condition["stage"], 2)
    elif True in set(status):
        return (stage_condition["stage"], 3)
    else:
        return (stage_condition["stage"], 1)
