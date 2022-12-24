# Generated by Django 4.1.4 on 2022-12-23 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookParking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('license_plate', models.CharField(max_length=100)),
                ('booking_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('booking_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Parkbay',
            fields=[
                ('bay_number', models.IntegerField(primary_key=True, serialize=False)),
                ('Booked', models.BooleanField(default=False)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
