# Generated by Django 2.1.5 on 2019-03-08 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("interactions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalinteraction",
            name="archived",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="historicalinteraction",
            name="archived_by",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="historicalinteraction",
            name="archived_on",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="historicalinteraction",
            name="archived_reason",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="interaction",
            name="archived",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="interaction",
            name="archived_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="interaction",
            name="archived_on",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="interaction",
            name="archived_reason",
            field=models.TextField(blank=True, null=True),
        ),
    ]
