# Generated by Django 3.1.2 on 2020-11-26 09:44

from django.db import migrations


def rename_assessment(apps, schema_editor):
    CachedHistoryItem = apps.get_model("history", "CachedHistoryItem")
    CachedHistoryItem.objects.filter(model="assessment", field__startswith="commercial").delete()
    CachedHistoryItem.objects.filter(model="assessment").update(model="economic_assessment")
    CachedHistoryItem.objects.filter(model="economic_assessment", field="impact").update(field="rating")


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_rename_public_barrier_country_to_location'),
        ('assessment', '0017_remove_user_analysis_data'),
        ('barriers', '0100_merge_20201124_1636'),
    ]

    operations = [
        migrations.RunPython(
            rename_assessment,
            reverse_code=migrations.RunPython.noop
        ),
    ]
