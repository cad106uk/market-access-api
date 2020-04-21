# Generated by Django 2.1.2 on 2018-12-05 14:32

from django.db import migrations, models

barrier_priorities = [
    {"code": "UNKNOWN", "name": "Unknown", "order": 0},
    {"code": "HIGH", "name": "High", "order": 1},
    {"code": "MEDIUM", "name": "Medium", "order": 2},
    {"code": "LOW", "name": "Low", "order": 3},
]


def add_update_barrier_priorities(apps, schema_editor):
    BarrierPriority = apps.get_model("metadata", "BarrierPriority")

    for item in barrier_priorities:
        try:
            priority = BarrierPriority.objects.get(code=item["code"])
            priority.name = item["name"]
            priority.order = item["order"]
            priority.save()
        except BarrierPriority.DoesNotExist:
            BarrierPriority(
                code=item["code"], name=item["name"], order=item["order"]
            ).save()


class Migration(migrations.Migration):

    dependencies = [("metadata", "0008_auto_20180928_1326")]

    operations = [
        migrations.CreateModel(
            name="BarrierPriority",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=10, unique=True)),
                ("name", models.CharField(max_length=25)),
                ("order", models.IntegerField()),
            ],
        ),
        migrations.RunPython(add_update_barrier_priorities),
    ]
