# Generated by Django 2.0.5 on 2018-06-07 13:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barriers', '0007_auto_20180606_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrier',
            name='commodity_codes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=None, max_length=10, null=True), null=True, size=None),
        ),
    ]
