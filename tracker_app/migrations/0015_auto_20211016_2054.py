# Generated by Django 3.2.8 on 2021-10-16 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0014_alter_company_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='switchgear',
            name='switchgear_parameters',
        ),
        migrations.AddField(
            model_name='switchgear',
            name='switchgear_parameters',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='tracker_app.switchgearparameters'),
            preserve_default=False,
        ),
    ]