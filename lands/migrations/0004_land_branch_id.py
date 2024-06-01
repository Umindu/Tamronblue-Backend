# Generated by Django 5.0.3 on 2024-05-11 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0001_initial'),
        ('lands', '0003_land_agent_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='branch_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='branches.branch'),
        ),
    ]