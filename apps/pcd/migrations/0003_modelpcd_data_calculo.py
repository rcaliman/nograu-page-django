# Generated by Django 5.0.1 on 2024-01-19 04:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcd', '0002_alter_modelpcd_codigo_banco_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelpcd',
            name='data_calculo',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]