# Generated by Django 4.1.4 on 2022-12-31 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Carpark', '0013_rename_baybooked_baybooking_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkbay',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Carpark.baybooking'),
        ),
    ]
