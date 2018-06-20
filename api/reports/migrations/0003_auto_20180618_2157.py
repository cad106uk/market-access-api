# Generated by Django 2.0.5 on 2018-06-18 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='is_resolved',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='report',
            name='support_type',
            field=models.PositiveIntegerField(choices=[(1, 'Market access team to take over the lead'), (
                2, 'Trade barriers team to guide me on next steps'), (3, "None, I'm going to hendle next steps myself")], null=True),
        ),
    ]
