# Generated by Django 2.2.16 on 2020-11-10 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soulcalibur_vi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='slug_source',
        ),
    ]
