# Generated by Django 2.1.11 on 2019-08-14 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rest_framework_sso", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sessiontoken",
            name="last_used_at",
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
