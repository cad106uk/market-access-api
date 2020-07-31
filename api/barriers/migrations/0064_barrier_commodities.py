# Generated by Django 2.2.13 on 2020-07-29 10:06

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commodities', '0002_auto_20200723_1020'),
        ('barriers', '0063_auto_20200428_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalbarrierinstance',
            name='commodities_cache',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(), default=list, size=None),
        ),
        migrations.CreateModel(
            name='BarrierCommodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('country', models.UUIDField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('barrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barrier_commodities', to='barriers.BarrierInstance')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barrier_commodities', to='commodities.Commodity')),
            ],
        ),
        migrations.AddField(
            model_name='barrierinstance',
            name='commodities',
            field=models.ManyToManyField(through='barriers.BarrierCommodity', to='commodities.Commodity'),
        ),
    ]
