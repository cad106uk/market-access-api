# Generated by Django 2.2.3 on 2019-08-07 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='export_value',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='historicalassessment',
            name='export_value',
            field=models.BigIntegerField(null=True),
        ),
    ]
