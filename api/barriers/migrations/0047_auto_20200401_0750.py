# Generated by Django 2.2.10 on 2020-04-01 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barriers', '0046_auto_20200327_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='barrierinstance',
            name='draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalbarrierinstance',
            name='draft',
            field=models.BooleanField(default=True),
        ),
    ]
