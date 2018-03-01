#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Producto
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    UpdateView,
    CreateView,
    DeleteView
    )
from django.core.urlresolvers import reverse_lazy
#mixins
from django.contrib.auth.mixins import(
    LoginRequiredMixin, PermissionRequiredMixin)
from django.contrib.auth.decorators import (
    login_required, permission_required)


class ProductoInsert(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
	permission_required = ('producto.add_producto')
	model = Producto
	success_url = reverse_lazy('producto:producto_list')
	fields = ['codigo', 'producto', 'descripcion',
	 'valorDP','valorVenta','valorDC','valorCC' ]

class ProductoList(LoginRequiredMixin, ListView):
    # login
    model = Producto
    context_object_name = 'productos'
    paginate_by = 5
    def get_queryset(self, *args, **kwargs):
        qs = super(ProductoList, self).get_queryset(*args, **kwargs).order_by("producto")
        return qs
        #funcion para paginar una lista
    def get_context_data(self, **kwargs):
        context = super(ProductoList, self). get_context_data(**kwargs)
        context['range'] = range(context["paginator"].num_pages)
        return context

class ProductoUpdate(LoginRequiredMixin,
                       PermissionRequiredMixin, UpdateView):
    permission_required = ('producto.change_producto')
    model = Producto
    success_url = reverse_lazy('producto:producto_list')
    fields = ['codigo', 'producto', 'descripcion',
              'valorDP','valorVenta','valorDC','valorCC']
#
# class InventarioDelete(LoginRequiredMixin,
#                        PermissionRequiredMixin, DeleteView):
# 	permission_required= ('inventario.delete_inventario')
# 	model = Inventario
# 	success_url = reverse_lazy('inventario:inventario_list')
#
@login_required()
def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    template = loader.get_template('producto/producto_detail.html')
    context = {
        'producto' : producto
    }
    return HttpResponse(template.render(context, request))
#
#
