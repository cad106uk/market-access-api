# Generated by Django 3.1.1 on 2020-09-01 15:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barriers', '0086_auto_20200827_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrierinstance',
            name='all_sectors',
            field=models.BooleanField(help_text='boolean to signify that all sectors are affected by this barrier', null=True),
        ),
        migrations.AlterField(
            model_name='barrierinstance',
            name='caused_by_trading_bloc',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='barrierinstance',
            name='companies',
            field=models.JSONField(default=None, help_text='list of companies that are affected', null=True),
        ),
        migrations.AlterField(
            model_name='barrierinstance',
            name='is_summary_sensitive',
            field=models.BooleanField(help_text='Does the summary contain sensitive information', null=True),
        ),
        migrations.AlterField(
            model_name='barrierinstance',
            name='sectors_affected',
            field=models.BooleanField(help_text='boolean to signify one or more sectors are affected by this barrier', null=True),
        ),
        migrations.AlterField(
            model_name='historicalbarrierinstance',
            name='all_sectors',
            field=models.BooleanField(help_text='boolean to signify that all sectors are affected by this barrier', null=True),
        ),
        migrations.AlterField(
            model_name='historicalbarrierinstance',
            name='caused_by_trading_bloc',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='historicalbarrierinstance',
            name='commodities_cache',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='historicalbarrierinstance',
            name='companies',
            field=models.JSONField(default=None, help_text='list of companies that are affected', null=True),
        ),
        migrations.AlterField(
            model_name='historicalbarrierinstance',
            name='is_summary_sensitive',
            field=models.BooleanField(help_text='Does the summary contain sensitive information', null=True),
        ),
        migrations.AlterField(
            model_name='historicalbarrierinstance',
            name='sectors_affected',
            field=models.BooleanField(help_text='boolean to signify one or more sectors are affected by this barrier', null=True),
        ),
        migrations.AlterField(
            model_name='historicalpublicbarrier',
            name='all_sectors',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='historicalpublicbarrier',
            name='published_versions',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='historicalpublicbarrier',
            name='trading_bloc',
            field=models.CharField(choices=[], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='publicbarrier',
            name='all_sectors',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='publicbarrier',
            name='published_versions',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='publicbarrier',
            name='trading_bloc',
            field=models.CharField(choices=[], max_length=7, null=True),
        ),
    ]
