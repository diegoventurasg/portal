# Generated by Django 3.0.8 on 2021-01-22 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0002_auto_20201104_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaborador',
            name='contato_de_emergencia_nome',
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='contato_de_emergencia_parentesco',
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='contato_de_emergencia_telefone',
        ),
    ]
