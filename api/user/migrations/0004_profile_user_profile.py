# Generated by Django 2.2 on 2019-05-15 11:01

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_internal'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_profile',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='temporary field to hold sso profile json object', null=True),
        ),
    ]
