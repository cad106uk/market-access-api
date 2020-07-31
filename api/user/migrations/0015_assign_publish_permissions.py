# Generated by Django 2.2.13 on 2020-06-30 13:44

from django.db import migrations


def assign_permissions(apps, schema_editor):
    Permission = apps.get_model("auth", "Permission")
    Group = apps.get_model("auth", "Group")
    Barrier = apps.get_model("barriers", "BarrierInstance")
    PublicBarrier = apps.get_model("barriers", "PublicBarrier")
    ContentType = apps.get_model("contenttypes", "ContentType")

    barrier_content_type = ContentType.objects.get_for_model(Barrier)
    public_barrier_content_type = ContentType.objects.get_for_model(PublicBarrier)

    change_barrier_public_eligibility, created = Permission.objects.get_or_create(
        codename="change_barrier_public_eligibility",
            defaults={
            "name": "Can change barrier public eligibility",
            "content_type": barrier_content_type
        }
    )
    change_publicbarrier, created = Permission.objects.get_or_create(
        codename="change_publicbarrier",
            defaults={
            "name": "Can change public barrier",
            "content_type": public_barrier_content_type
        }
    )
    mark_barrier_as_ready_for_publishing, created = Permission.objects.get_or_create(
        codename="mark_barrier_as_ready_for_publishing",
            defaults={
            "name": "Can mark barrier as ready for publishing",
            "content_type": public_barrier_content_type
        }
    )
    publish_barrier, created = Permission.objects.get_or_create(
        codename="publish_barrier",
            defaults={
            "name": "Can publish barrier",
            "content_type": public_barrier_content_type
        }
    )

    administrator_group = Group.objects.get(name="Administrator")
    administrator_group.permissions.add(
        change_barrier_public_eligibility,
        change_publicbarrier,
        mark_barrier_as_ready_for_publishing,
        publish_barrier,
    )

    sifter_group = Group.objects.get(name="Sifter")
    sifter_group.permissions.add(change_barrier_public_eligibility)

    editor_group = Group.objects.get(name="Editor")
    editor_group.permissions.add(
        change_barrier_public_eligibility,
        change_publicbarrier,
        mark_barrier_as_ready_for_publishing,
    )

    publisher_group = Group.objects.get(name="Publisher")
    publisher_group.permissions.add(
        change_barrier_public_eligibility,
        change_publicbarrier,
        mark_barrier_as_ready_for_publishing,
        publish_barrier,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('barriers', '0068_public_barrier_permissions'),
        ('user', '0014_assign_permissions'),
    ]

    operations = [
        migrations.RunPython(assign_permissions, reverse_code=migrations.RunPython.noop),
    ]
