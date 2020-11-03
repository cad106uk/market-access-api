# Generated by Django 3.1.2 on 2020-11-02 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barriers', '0091_auto_20201015_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barrierinstance',
            old_name='country_admin_areas',
            new_name='admin_areas',
        ),
        migrations.RenameField(
            model_name='barrierinstance',
            old_name='export_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='barrierinstance',
            old_name='barrier_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='barrierinstance',
            old_name='problem_status',
            new_name='term',
        ),
        migrations.RenameField(
            model_name='historicalbarrierinstance',
            old_name='country_admin_areas',
            new_name='admin_areas',
        ),
        migrations.RenameField(
            model_name='historicalbarrierinstance',
            old_name='export_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='historicalbarrierinstance',
            old_name='barrier_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='historicalbarrierinstance',
            old_name='problem_status',
            new_name='term',
        ),
    ]
