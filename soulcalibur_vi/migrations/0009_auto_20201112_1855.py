# Generated by Django 2.2.16 on 2020-11-12 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soulcalibur_vi', '0008_auto_20201112_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='height_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='soulcalibur_vi.HeightLevel'),
        ),
    ]
