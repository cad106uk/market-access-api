# Generated by Django 2.2.10 on 2020-03-27 16:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barriers', '0045_populate_categories_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrierinstance',
            name='sectors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), blank=True, default=list, help_text='list of sectors that are affected', size=None),
        ),
        migrations.AlterField(
            model_name='historicalbarrierinstance',
            name='sectors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), blank=True, default=list, help_text='list of sectors that are affected', size=None),
        ),
    ]
