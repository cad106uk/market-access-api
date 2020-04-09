# Generated by Django 2.2.8 on 2020-03-24 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barriers', '0040_merge_20200323_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarrierUserHit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_seen', models.DateTimeField(auto_now=True)),
                ('barrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barriers.BarrierInstance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'barrier')},
            },
        ),
    ]