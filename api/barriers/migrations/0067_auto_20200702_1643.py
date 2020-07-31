# Generated by Django 2.2.12 on 2020-07-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barriers', '0066_auto_20200629_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrierinstance',
            name='public_eligibility_summary',
            field=models.TextField(blank=True, default=None, help_text='Public eligibility summary if provided by user.', null=True),
        ),
        migrations.AlterField(
            model_name='historicalbarrierinstance',
            name='public_eligibility_summary',
            field=models.TextField(blank=True, default=None, help_text='Public eligibility summary if provided by user.', null=True),
        ),
    ]
