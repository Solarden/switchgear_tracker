# Generated by Django 3.2.8 on 2021-10-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0008_auto_20211012_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switchgearcomponents',
            name='serial_number',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='switchgearcomponents',
            name='supplier',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
