# Generated by Django 2.1 on 2018-08-30 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coda', '0004_auto_20180828_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paziente',
            name='rif',
            field=models.OneToOneField(auto_created=True, blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
