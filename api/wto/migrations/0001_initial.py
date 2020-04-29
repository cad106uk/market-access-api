# Generated by Django 2.2.11 on 2020-04-28 10:08

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interactions', '0007_merge_20200326_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='WTOCommittee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='WTOCommitteeGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='WTOProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('wto_has_been_notified', models.BooleanField()),
                ('wto_should_be_notified', models.NullBooleanField()),
                ('committee_notification_link', models.CharField(blank=True, max_length=255)),
                ('member_states', django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), blank=True, default=list, null=True, size=None)),
                ('raised_date', models.DateField(null=True)),
                ('case_number', models.CharField(blank=True, max_length=255)),
                ('committee_notification_document', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='committee_notification_wto_profiles', to='interactions.Document')),
                ('committee_notified', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='committee_notified_wto_profiles', to='wto.WTOCommittee')),
                ('committee_raised_in', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='committee_raised_in_wto_profiles', to='wto.WTOCommittee')),
                ('meeting_minutes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meeting_minutes_wto_profiles', to='interactions.Document')),
            ],
        ),
        migrations.AddField(
            model_name='wtocommittee',
            name='wto_committee_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='committees', to='wto.WTOCommitteeGroup'),
        ),
        migrations.CreateModel(
            name='HistoricalWTOProfile',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4)),
                ('wto_has_been_notified', models.BooleanField()),
                ('wto_should_be_notified', models.NullBooleanField()),
                ('committee_notification_link', models.CharField(blank=True, max_length=255)),
                ('member_states', django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), blank=True, default=list, null=True, size=None)),
                ('raised_date', models.DateField(null=True)),
                ('case_number', models.CharField(blank=True, max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('committee_notification_document', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='interactions.Document')),
                ('committee_notified', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='wto.WTOCommittee')),
                ('committee_raised_in', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='wto.WTOCommittee')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('meeting_minutes', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='interactions.Document')),
            ],
            options={
                'verbose_name': 'historical wto profile',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
