# Generated by Django 2.1.5 on 2019-04-10 08:54

from django.db import migrations

barrier_types_to_add = [
    {
        "title": "Tariffs or import duties",
        "description": "<p>Tariffs favour domestic firms over foreign competitors by increasing the price of goods. They can be resolved via unilateral reduction or multi/pluri-lateral agreements. Tariff schedules are available elsewhere, however specific tariffs that impact / are raised by UK businesses can be registered for business intelligence purposes.</p>",
        "category": "GOODS",
    },
]

barrier_types_to_edit = [
    {
        "old_title": "Tariffs and taxes imposed to protect or favour local suppliers",
        "new_title": "Specific taxes, other than tariffs, that are imposed to increase the price of goods.",
        "description": "<p>These might favour domestic firms over foreign competitors by being placed on imported products to make them more expensive than domestically produced alternative products.</p>",
        "category": "GOODSANDSERVICES",
    },
]


def add_barrier_types(apps, schema_editor):
    BarrierType = apps.get_model("metadata", "BarrierType")

    for item in barrier_types_to_add:
        try:
            barrier_type = BarrierType.objects.get(title=item["title"])
            barrier_type.description = item["description"]
            barrier_type.category = item["category"]
            barrier_type.save()
        except BarrierType.DoesNotExist:
            BarrierType(
                title=item["title"],
                description=item["description"],
                category=item["category"],
            ).save()

def edit_barrier_types(apps, schema_editor):
    BarrierType = apps.get_model("metadata", "BarrierType")

    for item in barrier_types_to_edit:
        try:
            barrier_type = BarrierType.objects.get(title=item["old_title"])
            barrier_type.title = item["new_title"]
            barrier_type.description = item["description"]
            barrier_type.category = item["category"]
            barrier_type.save()
        except BarrierType.DoesNotExist:
            BarrierType(
                title=item["new_title"],
                description=item["description"],
                category=item["category"],
            ).save()

class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0009_auto_20181205_1432'),
    ]

    operations = [
        migrations.RunPython(add_barrier_types),
        migrations.RunPython(edit_barrier_types),
    ]