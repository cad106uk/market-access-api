# Generated by Django 2.2.11 on 2020-05-13 09:49

from django.db import migrations


def clean_saved_search_filters(apps, schema_editor):
    SavedSearch = apps.get_model("user", "SavedSearch")

    # Convert search list to string
    for saved_search in SavedSearch.objects.filter(filters__search__isnull=False):
        if "search" in saved_search.filters and isinstance(saved_search.filters["search"], list):
            try:
                saved_search.filters["search"] = saved_search.filters["search"][0]
            except IndexError:
                saved_search.filters["search"] = ""
            saved_search.save()

    # Convert old createdBy field
    for saved_search in SavedSearch.objects.filter(filters__createdBy__isnull=False):
        if "createdBy" in saved_search.filters:
            created_by = saved_search.filters.pop("createdBy", [])
            if "1" in created_by:
                saved_search.filters["user"] = 1
            if "2" in created_by:
                saved_search.filters["team"] = 1
            saved_search.save()

    # Convert old created_by field
    for saved_search in SavedSearch.objects.filter(filters__created_by__isnull=False):
        if "created_by" in saved_search.filters:
            created_by = saved_search.filters.pop("created_by", [])
            if "1" in created_by:
                saved_search.filters["user"] = 1
            if "2" in created_by:
                saved_search.filters["team"] = 1
            saved_search.save()

    # Convert type field into category
    for saved_search in SavedSearch.objects.filter(filters__type__isnull=False):
        if "type" in saved_search.filters:
            saved_search.filters["category"] = saved_search.filters.pop("type")
            saved_search.save()


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_populate_saved_searches'),
    ]

    operations = [
        migrations.RunPython(
            clean_saved_search_filters,
            reverse_code=migrations.RunPython.noop
        ),
    ]
