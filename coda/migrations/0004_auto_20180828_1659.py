# Generated by Django 2.1 on 2018-08-28 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coda', '0003_auto_20180826_1615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paziente',
            options={'permissions': (('can_see_all', 'Can see all pazienti'), ('can_change_priority', 'Can change priority code of all pazienti'))},
        ),
    ]
