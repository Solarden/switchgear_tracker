# Generated by Django 3.2.8 on 2021-10-19 10:35

import django.core.files.storage
from django.db import migrations, models
import tracker_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0016_switchgear_stuff_missing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='media/logos/'), upload_to=tracker_app.models.company_logos_directory_path),
        ),
    ]