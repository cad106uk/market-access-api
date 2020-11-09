# Generated by Django 3.1.2 on 2020-11-05 17:32

from django.db import migrations


def convert_null_to_empty(apps, schema_editor):
    TeamMember = apps.get_model("documents", "Document")
    TeamMember.objects.filter(archived_reason__isnull=True).update(archived_reason="")


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20201015_1407'),
    ]

    operations = [
        migrations.RunPython(
            convert_null_to_empty,
            reverse_code=migrations.RunPython.noop
        ),
    ]