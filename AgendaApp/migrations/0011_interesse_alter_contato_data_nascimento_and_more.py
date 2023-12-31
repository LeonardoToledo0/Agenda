# Generated by Django 4.2.6 on 2023-11-06 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgendaApp', '0010_alter_telefone_iswatsapp_alter_telefone_ddd_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interesse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='contato',
            name='data_nascimento',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='IsWatsApp',
            field=models.BooleanField(verbose_name='Watsapp'),
        ),
    ]
