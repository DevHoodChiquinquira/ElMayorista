#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
#importar http
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
#Vistas
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    UpdateView,
    CreateView,
    DeleteView
    )
from django.contrib.auth.models import User
from .models import Factura, DetalleFactura
from django.core.urlresolvers import reverse_lazy
#mixins
from django.contrib.auth.mixins import(
    LoginRequiredMixin, PermissionRequiredMixin)
from django.contrib.auth.decorators import (
    login_required, permission_required)
#pdf Dionicio
import datetime
#por defecto se instala html5lib==0.999999999
#para que funciones pip install html5lib==1.0b8
import xhtml2pdf.pisa as pisa
import cStringIO as StringIO
from django import http
import cgi
#modelos
from cliente.models import Cliente
from producto.models import Producto
import json
import decimal
from django.core import serializers
#para facturaCrear
from django.template import RequestContext
from django.db import transaction
from django.contrib import messages
from django.template import RequestContext as ctx
from django.template import Context
from .forms import RangoForm
from django.utils import timezone

# Create your views here.
@login_required()
@permission_required('factura.add_factura')
def facturaCrear(request):
    form = None
#     if request.method == 'POST':
#         sid = transaction.savepoint()
#         try:
#             proceso = json.loads(request.POST.get('proceso'))
#             print proceso
#             print ("en try")
#             if 'clienProv' not in proceso:
#                 msg = 'El cliente no ha sido seleccionado'
#                 raise Exception(msg)
#
#             if len(proceso['producto']) <= 0:
#                 msg = 'No se ha seleccionado ningun producto'
#                 raise Exception(msg)
#
#             total = 0#factura cuando se crea inicia en 0
#
#             for k in proceso['producto']:
#                 print (k['codigo'])
#                 producto = Inventario.objects.get(codigo=k['codigo'])
#                 subtotal = (producto.valorVenta) * int(k['cantidad'])
#                 total +=subtotal
#                 #print ("en for")
#                 print(k['cantidad'])
#                 print producto
#                 #print subtotal
#                 #print total
#
#             crearFactura = Factura(
#                 cliente = Cliente.objects.get(dni=proceso['clienProv']),
#                 fecha = timezone.now(),
#                 total = total,
#                 vendedor = request.user,
#                 formaPago = proceso['tipoPago'],
#                 maquina = proceso['idMaquina'],
#             )
#             crearFactura.save()
#             print "Factura Guardada"
#             print crearFactura
#             for k in proceso['producto']:
#                 producto = Inventario.objects.get(codigo=k['codigo'])
#                 print("en for detalle")
#                 print (producto)
#                 crearDetalle = DetalleFactura(
#                     producto = producto,
#                     descripcion = producto.descripcion,
#                     cantidad = int(k['cantidad']),
#                     valorIva = producto.valorIva,
#                     precio = (producto.valorVenta - producto.valorIva) * int(k['cantidad']),
#                     subtotal = producto.valorVenta * int(k['cantidad']),
#                     factura = crearFactura,
#                 )
#                 crearDetalle.save()
#
#                 print("despues de crearDetalle.save()\n\n" )
#             messages.success(request, 'La venta se ha realizado')
# #ACA VOY
#         except Exception, e:
#             try:
#                 transaction.savepoint_rollback(sid)
#             except:
#                 pass
#             messages.error(request, e)

    return render(request, 'factura/crear_factura.html', {} )
    #return render_to_response('factura/crear_factura.html', {'form': form}, context_instance=RequestContext(request))



#Busqueda ajax de usuarios

def searchCliente(request):
    dni = request.GET.get('dni')
    dnis= Cliente.objects.filter(dni=dni)#__startswith
    dnis = [cliente_serializer(cliente) for cliente in dnis]
    return HttpResponse(json.dumps(dnis), content_type='application/json')

def cliente_serializer(cliente):
    return{'dni':cliente.dni, 'nombreEmpresa':cliente.nombreEmpresa,
           'nombreRepresentante':cliente.nombreRepresentante,
           'apellidoRepresentante':cliente.apellidoRepresentante}

#productos
def searchProducto(request):
    codigo = request.GET.get('codigo')
    codigos = Producto.objects.filter(codigo=codigo)
    json = serializers.serialize('json', codigos,
                                 fields= ('codigo', 'producto',
                                 'valorIva', 'valorVenta'))
    return HttpResponse(json, content_type='application/json')
