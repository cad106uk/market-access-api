# Generated by Django 2.2.3 on 2019-07-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaboration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalteammember',
            name='default',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teammember',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]
