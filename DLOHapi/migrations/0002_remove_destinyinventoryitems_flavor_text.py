# Generated by Django 4.0 on 2021-12-09 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DLOHapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinyinventoryitems',
            name='flavor_text',
        ),
    ]
