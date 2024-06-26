# Generated by Django 2.2.4 on 2019-11-05 00:42

from django.db import migrations, models
import django.db.models.deletion
import pretalx.common.models.mixins


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0021_auto_20190429_0750"),
        ("submission", "0040_submission_created_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="submissiontype",
            name="requires_access_code",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="track",
            name="requires_access_code",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="SubmitterAccessCode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("code", models.CharField(db_index=True, max_length=255)),
                ("valid_until", models.DateTimeField(blank=True, null=True)),
                (
                    "maximum_uses",
                    models.PositiveIntegerField(blank=True, default=1, null=True),
                ),
                ("redeemed", models.PositiveIntegerField(default=0)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="submitter_access_codes",
                        to="event.Event",
                    ),
                ),
                (
                    "submission_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="submitter_access_codes",
                        to="submission.SubmissionType",
                    ),
                ),
                (
                    "track",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="submitter_access_codes",
                        to="submission.Track",
                    ),
                ),
            ],
            options={
                "unique_together": {("event", "code")},
            },
            bases=(
                pretalx.common.models.mixins.LogMixin,
                pretalx.common.models.mixins.GenerateCode,
                models.Model,
            ),
        ),
        migrations.AddField(
            model_name="submission",
            name="access_code",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="submissions",
                to="submission.SubmitterAccessCode",
            ),
        ),
    ]
