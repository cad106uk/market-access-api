# Generated by Django 2.0.5 on 2018-09-26 08:04

from django.db import migrations

updated_report_stage_items = [
    {
        "code": "1.0",
        "description": "Report a barrier",
        "sub_items": [
            {"code": "1.1", "description": "Status of the barrier"},
            {"code": "1.2", "description": "Location of the barrier"},
            {"code": "1.3", "description": "Sectors affected by the barrier"},
            {"code": "1.4", "description": "About the barrier"},
        ],
    }
]


def update_report_stages(apps, schema_editor):
    Stage = apps.get_model("barriers", "Stage")
    for item in updated_report_stage_items:
        for sub_item in item["sub_items"]:
            try:
                sub_stage = Stage.objects.get(code=sub_item["code"])
                sub_stage.description = sub_item["description"]
                sub_stage.save()
            except Stage.DoesNotExist:
                pass


class Migration(migrations.Migration):

    dependencies = [("barriers", "0013_auto_20180924_1701")]

    operations = [migrations.RunPython(update_report_stages)]
