# Generated by Django 3.1.2 on 2020-11-05 17:36

from django.db import migrations


def convert_null_to_empty(apps, schema_editor):
    Interaction = apps.get_model("interactions", "Interaction")
    HistoricalInteraction = apps.get_model("interactions", "HistoricalInteraction")
    Document = apps.get_model("interactions", "Document")
    HistoricalDocument = apps.get_model("interactions", "HistoricalDocument")
    PublicBarrierNote = apps.get_model("interactions", "PublicBarrierNote")
    HistoricalPublicBarrierNote = apps.get_model("interactions", "HistoricalPublicBarrierNote")

    Interaction.objects.filter(archived_reason__isnull=True).update(archived_reason="")
    Interaction.objects.filter(text__isnull=True).update(text="")

    HistoricalInteraction.objects.filter(archived_reason__isnull=True).update(archived_reason="")
    HistoricalInteraction.objects.filter(text__isnull=True).update(text="")
    HistoricalInteraction.objects.filter(documents_cache__isnull=True).update(documents_cache=list())

    Document.objects.filter(mime_type__isnull=True).update(mime_type="")
    HistoricalDocument.objects.filter(mime_type__isnull=True).update(mime_type="")

    PublicBarrierNote.objects.filter(archived_reason__isnull=True).update(archived_reason="")
    HistoricalPublicBarrierNote.objects.filter(archived_reason__isnull=True).update(archived_reason="")


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0009_auto_20200901_1511'),
    ]

    operations = [
        migrations.RunPython(
            convert_null_to_empty,
            reverse_code=migrations.RunPython.noop
        ),
    ]