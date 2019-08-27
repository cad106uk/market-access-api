# Generated by Django 2.2.3 on 2019-08-07 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('barriers', '0032_auto_20190722_0905'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interactions', '0003_auto_20190322_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalAssessment',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_on', models.DateTimeField(blank=True, db_index=True, editable=False, null=True)),
                ('modified_on', models.DateTimeField(blank=True, editable=False, null=True)),
                ('archived', models.BooleanField(default=False)),
                ('archived_on', models.DateTimeField(blank=True, null=True)),
                ('archived_reason', models.TextField(blank=True, null=True)),
                ('impact', models.CharField(choices=[('HIGH', 'High'), ('MEDIUMHIGH', 'Medium High'), ('MEDIUMLOW', 'Medium Low'), ('LOW', 'Low')], max_length=25)),
                ('explanation', models.TextField()),
                ('value_to_economy', models.BigIntegerField(null=True)),
                ('import_market_size', models.BigIntegerField(null=True)),
                ('commercial_value', models.BigIntegerField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('archived_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('barrier', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='barriers.BarrierInstance')),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical assessment',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('archived', models.BooleanField(default=False)),
                ('archived_on', models.DateTimeField(blank=True, null=True)),
                ('archived_reason', models.TextField(blank=True, null=True)),
                ('impact', models.CharField(choices=[('HIGH', 'High'), ('MEDIUMHIGH', 'Medium High'), ('MEDIUMLOW', 'Medium Low'), ('LOW', 'Low')], max_length=25)),
                ('explanation', models.TextField()),
                ('value_to_economy', models.BigIntegerField(null=True)),
                ('import_market_size', models.BigIntegerField(null=True)),
                ('commercial_value', models.BigIntegerField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('archived_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('barrier', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='barriers.BarrierInstance')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('documents', models.ManyToManyField(help_text='assessment documents', related_name='assessment_documents', to='interactions.Document')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]