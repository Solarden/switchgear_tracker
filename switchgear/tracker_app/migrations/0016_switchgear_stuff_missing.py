# Generated by Django 3.2.8 on 2021-10-18 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0015_auto_20211016_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='switchgear',
            name='stuff_missing',
            field=models.BooleanField(default=False),
        ),
    ]
