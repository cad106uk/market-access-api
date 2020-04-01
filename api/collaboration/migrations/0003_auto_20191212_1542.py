# Generated by Django 2.2.8 on 2019-12-12 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collaboration', '0002_auto_20190730_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='barrier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barrier_team', to='barriers.BarrierInstance'),
        ),
    ]
