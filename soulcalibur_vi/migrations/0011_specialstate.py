# Generated by Django 2.2.16 on 2020-11-13 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soulcalibur_vi', '0010_auto_20201112_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('abbreviation', models.CharField(max_length=30, unique=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soulcalibur_vi.Character')),
            ],
        ),
    ]
