# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 00:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20170919_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(help_text='Nombre del Cliente', max_length=50)),
                ('client_email', models.CharField(help_text='Email del Cliente', max_length=60)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_date', models.DateField(help_text='Fecha de Vencimiento Servicio')),
                ('services_url', models.URLField(blank=True, help_text='Url de pago del servicio', null=True)),
                ('services_email_send', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.RenameModel(
            old_name='TipoServicio',
            new_name='TypeService',
        ),
        migrations.RemoveField(
            model_name='servicios',
            name='tipo_servicio',
        ),
        migrations.RemoveField(
            model_name='servicios',
            name='usuario',
        ),
        migrations.RenameField(
            model_name='typeservice',
            old_name='imagen',
            new_name='type_Services_image',
        ),
        migrations.RenameField(
            model_name='typeservice',
            old_name='nombre',
            new_name='type_services_name',
        ),
        migrations.RenameField(
            model_name='typeservice',
            old_name='url_default',
            new_name='type_services_url_default',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Servicios',
        ),
        migrations.AddField(
            model_name='services',
            name='services_type_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.TypeService'),
        ),
        migrations.AddField(
            model_name='services',
            name='services_user',
            field=models.ForeignKey(help_text='Usuario del Servicio', on_delete=django.db.models.deletion.CASCADE, to='services.Client'),
        ),
    ]
