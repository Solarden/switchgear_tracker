# Generated by Django 3.2.8 on 2021-10-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0020_alter_switchgear_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='contact_no1',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='contact_no2',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.CharField(max_length=64, null=True),
        ),
    ]