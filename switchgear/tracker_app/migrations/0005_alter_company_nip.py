# Generated by Django 3.2.8 on 2021-10-12 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0004_company_nip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='nip',
            field=models.CharField(max_length=13),
        ),
    ]
