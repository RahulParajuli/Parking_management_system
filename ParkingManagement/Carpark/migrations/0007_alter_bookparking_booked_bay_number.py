# Generated by Django 4.1.4 on 2022-12-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carpark', '0006_alter_bookparking_booked_bay_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookparking',
            name='Booked_bay_number',
            field=models.IntegerField(default=0),
        ),
    ]
