# Generated by Django 4.1.3 on 2022-12-18 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='podaci',
            old_name='Naziv_grada',
            new_name='Grad_podaci',
        ),
    ]
