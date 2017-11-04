# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Cliente(models.Model):
    TIPO_CUENTA = (
		('corriente', 'Corriente'),
		('ahorros', 'Ahorros'),
		('recaudo','Recaudo'),
		)
    dni = models.CharField(max_length=15,
        unique=True, verbose_name= 'Número de Identificación')
    nombreEmpresa = models.CharField(max_length=45, null=True, blank=True,
        verbose_name= 'Nombre empresa')
    nombreRepresentante = models.CharField(max_length=45,
        verbose_name= 'Nombre representante')
    apellidoRepresentante = models.CharField(max_length=45,
        verbose_name = 'Apellido representante')
    telefono = PhoneNumberField (default='+573041234567',
        verbose_name = 'Teléfono')
    correo = models.EmailField(max_length=100, blank=True, null=True,
        verbose_name='Correo')
    ciudad = models.CharField(max_length=25, blank=True, null=True,
        verbose_name=' Ciudad')
    direccion = models.CharField(max_length=25, blank=True, null=True,
        verbose_name='Dirección')
    banco = models.CharField(max_length=45, blank=True, null=True)
    tipoCuenta = models.CharField(choices=TIPO_CUENTA, max_length=25,
        blank=True, null=True, verbose_name='Tipo de cuenta')
    numeroCuenta = models.CharField(max_length=15, blank=True,
        null=True, verbose_name='Número de cuenta')

    def __unicode__(self):
        return self.dni
