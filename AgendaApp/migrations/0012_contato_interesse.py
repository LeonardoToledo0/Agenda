# Generated by Django 4.2.6 on 2023-11-06 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgendaApp', '0011_interesse_alter_contato_data_nascimento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='Interesse',
            field=models.ManyToManyField(to='AgendaApp.interesse'),
        ),
    ]
