# Generated by Django 2.2.10 on 2020-04-03 10:46

from django.db import migrations


def delete_stale_report_stages(apps, schema_editor):
    BarrierReportStage = apps.get_model('barriers', 'BarrierReportStage')
    BarrierReportStage.objects.exclude(barrier__draft=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('barriers', '0048_populate_draft'),
    ]

    operations = [
        migrations.RunPython(
            delete_stale_report_stages,
            reverse_code=migrations.RunPython.noop
        ),
    ]
