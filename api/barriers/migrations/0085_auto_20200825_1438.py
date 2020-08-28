# Generated by Django 2.2.13 on 2020-08-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barriers', '0084_auto_20200814_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='barrierinstance',
            name='caused_by_trading_bloc',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='barrierinstance',
            name='trading_bloc',
            field=models.CharField(choices=[('TB00016', 'European Union')], max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='historicalbarrierinstance',
            name='caused_by_trading_bloc',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='historicalbarrierinstance',
            name='trading_bloc',
            field=models.CharField(choices=[('TB00016', 'European Union')], max_length=7, null=True),
        ),
    ]
