# Generated by Django 3.0.8 on 2021-03-23 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0003_auto_20210323_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servidor',
            name='vm_template',
        ),
        migrations.AddField(
            model_name='servidor',
            name='vm_ambiente_virtual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vm_ambiente_virtual', to='infra.AmbienteVirtual'),
        ),
    ]
