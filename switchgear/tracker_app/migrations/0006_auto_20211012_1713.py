# Generated by Django 3.2.8 on 2021-10-12 17:13

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0005_alter_company_nip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='media/logos/'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='switchgearparameters',
            name='par_hz',
            field=models.CharField(max_length=16),
        ),
    ]