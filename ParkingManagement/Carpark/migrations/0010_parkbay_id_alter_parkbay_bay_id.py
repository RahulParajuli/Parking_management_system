# Generated by Django 4.1.4 on 2022-12-23 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carpark', '0009_alter_parkbay_bay_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkbay',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parkbay',
            name='bay_id',
            field=models.IntegerField(auto_created=True),
        ),
    ]
