# Generated by Django 4.1.3 on 2023-02-22 12:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_grad_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='podaci',
            options={'ordering': ['Datum', 'Dio_dana', 'Grad_podaci__Naziv_grada']},
        ),
        migrations.AlterField(
            model_name='podaci',
            name='Vjetar_brzina',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
