# Generated by Django 5.2 on 2025-04-15 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('difficulty', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
