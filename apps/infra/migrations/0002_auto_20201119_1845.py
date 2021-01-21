# Generated by Django 3.0.8 on 2020-11-19 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='tipo_uso',
            field=models.CharField(choices=[('', ''), ('OPERACIONAL', 'OPERACIONAL'), ('DESENVOLVIMENTO', 'DESENVOLVIMENTO'), ('PESQUISA', 'PESQUISA'), ('DOCUMENTO', 'DOCUMENTO')], max_length=255, verbose_name='Tipo de Uso'),
        ),
    ]
