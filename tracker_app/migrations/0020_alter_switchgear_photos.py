# Generated by Django 3.2.8 on 2021-10-19 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0019_switchgear_has_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switchgear',
            name='photos',
            field=models.ManyToManyField(blank=True, to='tracker_app.SwitchgearPhotos'),
        ),
    ]