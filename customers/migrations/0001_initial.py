# Generated by Django 5.0.4 on 2024-05-01 02:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branches', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(default='', max_length=10)),
                ('nic', models.CharField(default='', max_length=12)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.CharField(default='', max_length=10)),
                ('address', models.TextField(default='')),
                ('city', models.CharField(default='', max_length=255)),
                ('counrty', models.CharField(default='', max_length=255)),
                ('zip_code', models.CharField(default='', max_length=10)),
                ('staus', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('agent_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('branch_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='branches.branch')),
            ],
        ),
    ]
