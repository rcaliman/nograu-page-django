# Generated by Django 5.0.1 on 2024-01-08 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikefit', '0006_modelbikefitabout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelbikefitabout',
            name='nome',
            field=models.CharField(max_length=250),
        ),
    ]
