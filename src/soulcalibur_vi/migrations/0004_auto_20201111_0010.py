# Generated by Django 2.2.16 on 2020-11-11 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soulcalibur_vi', '0003_character_slug_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialstance',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
