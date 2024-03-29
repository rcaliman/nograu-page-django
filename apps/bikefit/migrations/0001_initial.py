# Generated by Django 4.2.1 on 2024-03-23 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelBikefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cavalo', models.FloatField()),
                ('esterno', models.FloatField()),
                ('braco', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('data', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Cálculos de bikefit',
                'verbose_name_plural': 'Cálculos de bikefit',
            },
        ),
        migrations.CreateModel(
            name='ModelBikefitAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('nome', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Sobre',
                'verbose_name_plural': 'Sobre',
            },
        ),
        migrations.CreateModel(
            name='ModelBikefitLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=250)),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'Lista de Links',
                'verbose_name_plural': 'Lista de Links',
            },
        ),
    ]
