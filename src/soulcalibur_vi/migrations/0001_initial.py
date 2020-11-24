# Generated by Django 2.2.16 on 2020-11-10 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('date_time_db_entry', models.DateTimeField(auto_now=True)),
                ('date_time_version', models.DateTimeField()),
                ('slug_source', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialStance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Special Stance', max_length=30)),
                ('abbreviation', models.CharField(default='', max_length=60)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soulcalibur_vi.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(default='8WayRun', max_length=30)),
                ('type_entry', models.CharField(blank=True, max_length=30, null=True)),
                ('frames_to_impact', models.CharField(blank=True, max_length=30, null=True)),
                ('base_damage', models.CharField(blank=True, max_length=30, null=True)),
                ('attack_name', models.CharField(blank=True, max_length=60, null=True)),
                ('command', models.CharField(max_length=60)),
                ('soulcharge_chip_damage', models.CharField(blank=True, max_length=30, null=True)),
                ('height_level', models.CharField(blank=True, max_length=30, null=True)),
                ('recovery_on_guard', models.CharField(blank=True, max_length=30, null=True)),
                ('recovery_on_hit', models.CharField(blank=True, max_length=30, null=True)),
                ('recovery_on_counter_hit', models.CharField(blank=True, max_length=30, null=True)),
                ('guard_burst_damage', models.CharField(blank=True, max_length=30, null=True)),
                ('notes', models.TextField(blank=True, max_length=240, null=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soulcalibur_vi.Character')),
            ],
        ),
    ]
