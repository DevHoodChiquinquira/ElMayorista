# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Factura, DetalleFactura

@admin.register(Factura)
class AdminFactura(admin.ModelAdmin):
	list_display = ( 'maquina', 'fecha',
		'vendedor', 'cliente', 'iva', 'total',)

@admin.register(DetalleFactura)
class AdminDetalleFactura(admin.ModelAdmin):
	list_display = ('factura', 'producto', 'cantidad', 'precio',
		'valorIva', 'subtotal',)
