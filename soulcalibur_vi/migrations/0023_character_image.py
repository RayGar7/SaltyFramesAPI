# Generated by Django 3.1.3 on 2021-01-02 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soulcalibur_vi', '0022_auto_20201209_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='image',
            field=models.FileField(blank=True, upload_to='sc-characters'),
        ),
    ]
