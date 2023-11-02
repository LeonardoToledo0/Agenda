# Generated by Django 4.2.6 on 2023-11-02 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgendaApp', '0009_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefone',
            name='IsWatsApp',
            field=models.BooleanField(verbose_name='Tem Watsapp ?'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='ddd',
            field=models.IntegerField(max_length=2, verbose_name='DDD'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='tipo',
            field=models.CharField(choices=[('RES', 'Residencial'), ('COM', 'Comercial'), ('REC', 'Recado'), ('CEL', 'Celular')], max_length=3),
        ),
    ]
