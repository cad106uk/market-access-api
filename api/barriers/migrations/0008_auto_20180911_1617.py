# Generated by Django 2.0.5 on 2018-09-11 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("barriers", "0007_auto_20180905_1553")]

    operations = [
        migrations.RemoveField(model_name="barrierstatus", name="barrier"),
        migrations.RemoveField(model_name="barrierstatus", name="created_by"),
        migrations.DeleteModel(name="BarrierStatus"),
    ]
