# Generated by Django 2.2.11 on 2020-04-03 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barriers', '0054_convert_to_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barrierinstance',
            name='eu_exit_related',
        ),
        migrations.RemoveField(
            model_name='historicalbarrierinstance',
            name='eu_exit_related',
        ),
    ]
