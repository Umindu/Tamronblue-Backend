# Generated by Django 5.0.3 on 2024-05-11 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='google_map',
            field=models.CharField(default='', max_length=400),
        ),
    ]
