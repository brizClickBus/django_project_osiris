# Generated by Django 4.1.5 on 2023-02-04 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Extrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seguimento', models.CharField(max_length=225)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('forma_pagamento', models.CharField(max_length=225)),
                ('tipo_gasto', models.BooleanField()),
                ('date', models.DateField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Seguimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=225)),
                ('tipo_seguimento', models.CharField(choices=[('FIXO', 'Fixo'), ('VARIADO', 'Variado')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
