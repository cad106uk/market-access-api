# Generated by Django 2.0.5 on 2018-06-06 10:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barriers', '0004_auto_20180531_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='barriercommoditycode',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='barrier',
            name='commodity_codes',
        ),
        migrations.AddField(
            model_name='barrier',
            name='commodity_codes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(
                blank=True, default=None, max_length=10, null=True), null=True, size=None),
            preserve_default=False,
        ),
    ]
