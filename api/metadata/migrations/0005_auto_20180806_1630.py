# Generated by Django 2.0.5 on 2018-08-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("metadata", "0004_auto_20180724_0808")]

    operations = [
        migrations.AlterField(
            model_name="barriertype", name="description", field=models.TextField()
        )
    ]
