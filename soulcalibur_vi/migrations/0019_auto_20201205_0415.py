# Generated by Django 3.1.3 on 2020-12-05 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soulcalibur_vi', '0018_auto_20201116_0132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='slug_source',
            new_name='slug',
        ),
    ]
