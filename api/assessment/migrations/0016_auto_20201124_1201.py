# Generated by Django 3.1.2 on 2020-11-24 12:01

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0015_migrate_old_assessments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='economicassessment',
            old_name='analysis_data',
            new_name='user_analysis_data',
        ),
        migrations.RenameField(
            model_name='historicaleconomicassessment',
            old_name='analysis_data',
            new_name='user_analysis_data',
        ),
        migrations.AddField(
            model_name='economicassessment',
            name='automated_analysis_data',
            field=models.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
        migrations.AddField(
            model_name='historicaleconomicassessment',
            name='automated_analysis_data',
            field=models.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
    ]
