# Generated by Django 2.2.11 on 2020-04-28 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wto', '0001_initial'),
        ('barriers', '0062_auto_20200421_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='barrierinstance',
            name='wto_profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='barrier', to='wto.WTOProfile'),
        ),
        migrations.AddField(
            model_name='historicalbarrierinstance',
            name='wto_profile',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='wto.WTOProfile'),
        ),
    ]
