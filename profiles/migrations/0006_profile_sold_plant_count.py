# Generated by Django 5.0.3 on 2024-05-27 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_is_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sold_plant_count',
            field=models.IntegerField(default=0),
        ),
    ]
