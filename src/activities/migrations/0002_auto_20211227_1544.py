# Generated by Django 2.2 on 2021-12-27 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='schedule',
            field=models.DateTimeField(help_text='Formato: aaaa-mm-dd HH:MM:SS', verbose_name='Calendario'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='status',
            field=models.CharField(choices=[('active', 'Activo'), ('deactivated', 'Inactivo'), ('cancelled', 'Cancelado'), ('rescheduled', 'Re-agendado'), ('done', 'Finalizada')], default='active', max_length=35, verbose_name='Estatus'),
        ),
        migrations.AlterField(
            model_name='property',
            name='disabled_at',
            field=models.DateTimeField(blank=True, help_text='Formato: aaaa-mm-dd HH:MM:SS', null=True, verbose_name='Inactivar'),
        ),
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('active', 'Activo'), ('deactivated', 'Inactivo'), ('cancelled', 'Cancelado'), ('rescheduled', 'Re-agendado'), ('done', 'Finalizada')], default='active', max_length=35, verbose_name='Estatus'),
        ),
    ]
