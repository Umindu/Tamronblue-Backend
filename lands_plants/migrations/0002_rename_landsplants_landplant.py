# Generated by Django 5.0.4 on 2024-05-01 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0001_initial'),
        ('lands_plants', '0001_initial'),
        ('plants', '0002_plant_created_at_plant_updated_at'),
        ('varieties', '0002_alter_variety_plant_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LandsPlants',
            new_name='LandPlant',
        ),
    ]
