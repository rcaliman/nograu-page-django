# Generated by Django 5.0.1 on 2024-01-08 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikefit', '0005_alter_modelbikefit_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelBikefitAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('nome', models.TextField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Sobre',
                'verbose_name_plural': 'Sobre',
            },
        ),
    ]
