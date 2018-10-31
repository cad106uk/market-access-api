# Generated by Django 2.1.2 on 2018-10-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barriers', '0019_merge_20181023_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='barrierinstance',
            name='code',
            field=models.CharField(help_text='readable reference code', max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='historicalbarrierinstance',
            name='code',
            field=models.CharField(db_index=True, help_text='readable reference code', max_length=255, null=True),
        ),
    ]
