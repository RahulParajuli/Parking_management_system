# Generated by Django 4.1.4 on 2022-12-23 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carpark', '0010_parkbay_id_alter_parkbay_bay_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkbay',
            name='id',
        ),
        migrations.AlterField(
            model_name='parkbay',
            name='bay_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]