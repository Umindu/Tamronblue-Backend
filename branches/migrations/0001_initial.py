# Generated by Django 5.0.4 on 2024-05-01 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=300)),
                ('district', models.CharField(default='', max_length=100)),
                ('agricultural_zone', models.CharField(default='', max_length=100)),
                ('region', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
