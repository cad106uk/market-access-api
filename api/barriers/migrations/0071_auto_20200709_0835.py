# Generated by Django 2.2.12 on 2020-07-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barriers', '0070_auto_20200706_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpublicbarrier',
            name='internal_summary_at_update',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalpublicbarrier',
            name='internal_title_at_update',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='publicbarrier',
            name='internal_summary_at_update',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='publicbarrier',
            name='internal_title_at_update',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
