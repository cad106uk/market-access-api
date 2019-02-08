# Generated by Django 2.1.5 on 2019-01-31 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

report_stage_items = [
    {
        "code": "1.0",
        "description": "Add a barrier",
        "sub_items": [
            {"code": "1.1", "description": "Urgency of the problem"},
            {"code": "1.2", "description": "Location of the barrier"},
            {"code": "1.3", "description": "Sectors affected by the barrier"},
            {"code": "1.4", "description": "About the barrier"},
            {"code": "1.5", "description": "Summarise the problem"},
        ],
    }
]

def add_report_stages(apps, schema_editor):
    Stage = apps.get_model("barriers", "Stage")
    for item in report_stage_items:
        parent_stage = Stage.objects.get(code=item["code"])
        parent_stage.description = item["description"]
        parent_stage.save()
        for sub_item in item["sub_items"]:
            try:
                sub_stage = Stage.objects.get(code=sub_item["code"])
                sub_stage.description = sub_item["description"]
                sub_stage.save()
            except Stage.DoesNotExist:
                Stage(
                    code=sub_item["code"],
                    description=sub_item["description"],
                    parent=parent_stage,
                ).save()


class Migration(migrations.Migration):

    dependencies = [
        ("barriers", "0024_auto_20190131_1542"),
    ]
    operations = [
        migrations.RunPython(add_report_stages),
    ]
