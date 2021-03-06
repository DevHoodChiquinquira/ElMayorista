# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-04 00:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('producto', '0003_auto_20171103_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=45, verbose_name='Descripci\xf3n')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=15)),
                ('cantidad', models.PositiveSmallIntegerField()),
                ('valorIva', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor IVA')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('serie', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('maquina', models.CharField(max_length=20, verbose_name='M\xe1quina')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('formaPago', models.CharField(choices=[('efectivo', 'Efectivo'), ('cheque', 'Cheque'), ('tarjeta d\xe9bito', 'Tarjeta d\xe9bito'), ('tarjeta cr\xe9dito', 'Tarjeta cr\xe9dito'), ('venta a cr\xe9dito', 'Venta a cr\xe9dito'), ('bono', 'Bono'), ('vale', 'Vale'), ('otros', 'Otros')], max_length=50, verbose_name='Forma de pago')),
                ('iva', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='factura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.Factura'),
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Producto'),
        ),
    ]
