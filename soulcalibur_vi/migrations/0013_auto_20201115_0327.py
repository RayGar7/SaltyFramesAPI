# Generated by Django 2.2.16 on 2020-11-15 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soulcalibur_vi', '0012_auto_20201115_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialstate',
            name='abbreviation',
            field=models.CharField(max_length=30),
        ),
    ]
