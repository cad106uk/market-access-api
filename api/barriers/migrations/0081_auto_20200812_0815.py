# Generated by Django 2.2.13 on 2020-08-12 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barriers', '0080_auto_20200806_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrierinstance',
            name='wto_profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wto.WTOProfile'),
        ),
    ]