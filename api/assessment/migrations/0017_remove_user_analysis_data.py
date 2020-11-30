# Generated by Django 3.1.2 on 2020-11-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0011_fix_blank_and_null'),
        ('assessment', '0016_auto_20201124_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='economicassessment',
            name='user_analysis_data',
        ),
        migrations.RemoveField(
            model_name='historicaleconomicassessment',
            name='user_analysis_data',
        ),
        migrations.AlterField(
            model_name='economicassessment',
            name='documents',
            field=models.ManyToManyField(related_name='economic_assessments', to='interactions.Document'),
        ),
    ]
