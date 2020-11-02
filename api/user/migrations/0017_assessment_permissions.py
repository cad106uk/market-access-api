# Generated by Django 3.1.2 on 2020-10-27 09:45

from django.contrib.auth.management import create_permissions
from django.db import migrations


def migrate_permissions(apps, schema_editor):
    """
    Ensure model permissions have been created
    """
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None


def add_roles(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.create(name="Analyst")
    Group.objects.create(name="Assessment approver")


def delete_roles(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name="Analyst").delete()
    Group.objects.filter(name="Assessment approver").delete()


def assign_permissions(apps, schema_editor):
    Permission = apps.get_model("auth", "Permission")
    Group = apps.get_model("auth", "Group")
    ContentType = apps.get_model("contenttypes", "ContentType")
    User = apps.get_model("auth", "User")

    user_content_type = ContentType.objects.get_for_model(User)

    add_ra_permission = Permission.objects.get(codename="add_resolvabilityassessment")
    change_ra_permission = Permission.objects.get(codename="change_resolvabilityassessment")
    archive_ra_permission = Permission.objects.get(codename="archive_resolvabilityassessment")
    approve_ra_permission = Permission.objects.get(codename="approve_resolvabilityassessment")

    add_sa_permission = Permission.objects.get(codename="add_strategicassessment")
    change_sa_permission = Permission.objects.get(codename="change_strategicassessment")
    archive_sa_permission = Permission.objects.get(codename="archive_strategicassessment")
    approve_sa_permission = Permission.objects.get(codename="approve_strategicassessment")

    administrator_group = Group.objects.get(name="Administrator")
    administrator_group.permissions.add(
        add_ra_permission,
        change_ra_permission,
        archive_ra_permission,
        approve_ra_permission,
        add_sa_permission,
        change_sa_permission,
        archive_sa_permission,
        approve_sa_permission,
    )

    approver_group = Group.objects.get(name="Assessment approver")
    approver_group.permissions.add(
        add_ra_permission,
        change_ra_permission,
        archive_ra_permission,
        approve_ra_permission,
        add_sa_permission,
        change_sa_permission,
        archive_sa_permission,
        approve_sa_permission,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20200901_1511'),
        ('assessment', '0009_resolvability_and_strategic_assessments'),
    ]

    operations = [
        migrations.RunPython(migrate_permissions, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(add_roles, reverse_code=delete_roles),
        migrations.RunPython(assign_permissions, reverse_code=migrations.RunPython.noop),
    ]
