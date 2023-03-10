# Generated by Django 4.1.5 on 2023-02-06 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('banco', '0002_limites_chequeespecial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartao_alimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=225)),
                ('tipo', models.CharField(choices=[('VR', 'VR'), ('VA', 'VA'), ('CRÉDITO', 'Crédito'), ('OUTROS', 'Outros')], max_length=20)),
                ('createdAt', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Extrado_alimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.cartao_alimentacao')),
            ],
        ),
        migrations.CreateModel(
            name='Entradas_alimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dataEntrada', models.DateTimeField()),
                ('cartao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.cartao_alimentacao')),
            ],
        ),
    ]
