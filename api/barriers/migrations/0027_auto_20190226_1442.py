# Generated by Django 2.1.5 on 2019-02-26 14:42

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("barriers", "0026_auto_20190205_2329")]

    operations = [
        migrations.AddField(
            model_name="barrierinstance",
            name="country_admin_areas",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.UUIDField(),
                blank=True,
                default=None,
                help_text="list of states, provinces, regions etc within a country",
                null=True,
                size=None,
            ),
        ),
        migrations.AddField(
            model_name="historicalbarrierinstance",
            name="country_admin_areas",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.UUIDField(),
                blank=True,
                default=None,
                help_text="list of states, provinces, regions etc within a country",
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="barrierinstance",
            name="companies",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                default=None, help_text="list of companies that are affected", null=True
            ),
        ),
        migrations.AlterField(
            model_name="barrierinstance",
            name="problem_status",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "A problem that is blocking a specific export or investment"),
                    (
                        2,
                        "A strategic barrier likely to affect multiple exports or sectors",
                    ),
                ],
                help_text="type of problem, long term or short term",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="barrierinstance",
            name="sectors",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.UUIDField(),
                blank=True,
                default=None,
                help_text="list of sectors that are affected",
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="historicalbarrierinstance",
            name="companies",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                default=None, help_text="list of companies that are affected", null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalbarrierinstance",
            name="problem_status",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "A problem that is blocking a specific export or investment"),
                    (
                        2,
                        "A strategic barrier likely to affect multiple exports or sectors",
                    ),
                ],
                help_text="type of problem, long term or short term",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalbarrierinstance",
            name="sectors",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.UUIDField(),
                blank=True,
                default=None,
                help_text="list of sectors that are affected",
                null=True,
                size=None,
            ),
        ),
    ]
