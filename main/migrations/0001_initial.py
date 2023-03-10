# Generated by Django 4.1.3 on 2022-12-17 17:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Postanski_broj', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)])),
                ('Naziv_grada', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Meteoroloska_stanica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sifra_stanice', models.CharField(max_length=5)),
                ('Naziv_stanice', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Zupanija_Provincija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sifra_zupanije_provincije', models.CharField(max_length=5)),
                ('Ime_Zupanije_provincije', models.CharField(max_length=30)),
                ('Stanica', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.meteoroloska_stanica')),
            ],
        ),
        migrations.CreateModel(
            name='Podaci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temperatura_u_C', models.FloatField()),
                ('Vjetar_brzina', models.IntegerField()),
                ('Oborine', models.FloatField()),
                ('Vlaznost', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('Datum', models.DateField()),
                ('Opis_vremena', models.CharField(max_length=15, verbose_name='Kratak opis vremena')),
                ('Naziv_grada', models.ManyToManyField(to='main.grad')),
            ],
        ),
        migrations.AddField(
            model_name='grad',
            name='Zupanija_Provincija_County',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.zupanija_provincija'),
        ),
    ]
