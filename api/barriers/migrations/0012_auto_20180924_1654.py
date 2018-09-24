# Generated by Django 2.0.5 on 2018-09-24 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barriers', '0011_historicalbarriercompany_historicalbarriercontributor_historicalbarrierinstance_historicalbarrierint'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='barriercompany',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='barriercompany',
            name='barrier',
        ),
        migrations.RemoveField(
            model_name='barriercompany',
            name='company',
        ),
        migrations.RemoveField(
            model_name='barriercompany',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='barriercompany',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='historicalbarriercompany',
            name='barrier',
        ),
        migrations.RemoveField(
            model_name='historicalbarriercompany',
            name='company',
        ),
        migrations.RemoveField(
            model_name='historicalbarriercompany',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicalbarriercompany',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalbarriercompany',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='barrierinstance',
            name='companies',
        ),
        migrations.DeleteModel(
            name='BarrierCompany',
        ),
        migrations.DeleteModel(
            name='DatahubCompany',
        ),
        migrations.DeleteModel(
            name='HistoricalBarrierCompany',
        ),
    ]
