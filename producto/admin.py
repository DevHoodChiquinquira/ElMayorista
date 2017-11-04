# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class AdminProducto(admin.ModelAdmin):
	list_display = ('codigo', 'producto', 'cantidad',
		'descripcion', 'valorCompra', 'valorIva',
		'valorVenta',)
