# Generated by Django 3.1.3 on 2021-02-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soulcalibur_vi', '0024_auto_20210203_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='frames_to_impact',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]