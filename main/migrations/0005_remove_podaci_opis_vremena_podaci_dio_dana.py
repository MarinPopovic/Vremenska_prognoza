# Generated by Django 4.1.3 on 2022-12-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_podaci_grad_podaci'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podaci',
            name='Opis_vremena',
        ),
        migrations.AddField(
            model_name='podaci',
            name='Dio_dana',
            field=models.CharField(default=0, max_length=15),
        ),
    ]