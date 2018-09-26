# Generated by Django 2.0.5 on 2018-09-11 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barriers', '0008_auto_20180911_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='barrierinstance',
            name='commercial_sensitivities',
            field=models.TextField(default=None, help_text='Commercial or confidentiality sensitivities to be aware of', null=True),
        ),
        migrations.AddField(
            model_name='barrierinstance',
            name='fta_infringement',
            field=models.NullBooleanField(default=None, help_text='Legal obligations infringed'),
        ),
        migrations.AddField(
            model_name='barrierinstance',
            name='has_legal_infringement',
            field=models.PositiveIntegerField(choices=[(1, 'Yes'), (2, 'No'), (3, "Don't know")], default=None, help_text='Legal obligations infringed', null=True),
        ),
        migrations.AddField(
            model_name='barrierinstance',
            name='infringement_summary',
            field=models.TextField(default=None, help_text='Summary of infringments', null=True),
        ),
        migrations.AddField(
            model_name='barrierinstance',
            name='other_infringement',
            field=models.NullBooleanField(default=None, help_text='Legal obligations infringed'),
        ),
        migrations.AddField(
            model_name='barrierinstance',
            name='political_sensitivities',
            field=models.TextField(default=None, help_text='Political sensitivities to be aware of', null=True),
        ),
        migrations.AddField(
            model_name='barrierinstance',
            name='wto_infringement',
            field=models.NullBooleanField(default=None, help_text='Legal obligations infringed'),
        ),
    ]