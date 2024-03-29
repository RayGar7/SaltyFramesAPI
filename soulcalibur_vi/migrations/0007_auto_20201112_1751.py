# Generated by Django 2.2.16 on 2020-11-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soulcalibur_vi', '0006_auto_20201112_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heightlevel',
            name='abbreviation',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='heightlevel',
            name='name',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
    ]
