# Generated by Django 3.1.2 on 2020-11-09 16:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barriers', '0096_fix_blank_and_null'),
        ('interactions', '0011_fix_blank_and_null'),
        ('assessment', '0012_fix_blank_and_null'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assessment',
            new_name='EconomicAssessment',
        ),
        migrations.RenameModel(
            old_name='HistoricalAssessment',
            new_name='HistoricalEconomicAssessment',
        ),
        migrations.AlterModelOptions(
            name='historicaleconomicassessment',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical economic assessment'},
        ),
    ]