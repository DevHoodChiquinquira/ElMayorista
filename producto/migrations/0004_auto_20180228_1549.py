# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-28 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_auto_20171103_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='ValorCC',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=15, null=True, verbose_name='Valor consumo caja'),
        ),
        migrations.AddField(
            model_name='producto',
            name='valorDC',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=15, null=True, verbose_name='Valor distribuidor caja'),
        ),
        migrations.AddField(
            model_name='producto',
            name='valorDP',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=15, null=True, verbose_name='Valor distribuidor paquete'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='valorVenta',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='Valor consumo paquete'),
        ),
    ]
