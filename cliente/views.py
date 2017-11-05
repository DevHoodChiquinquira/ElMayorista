# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import (
    UpdateView, CreateView, DeleteView)
from django.views.generic import ListView
from .models import Cliente
#from .forms import PerfilForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
#Permisos
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin)
from django.contrib.auth.decorators import (
    login_required, permission_required)


class ClienteInsert(LoginRequiredMixin,
                    PermissionRequiredMixin, CreateView):
    permission_required = ('cliente.add_cliente')
    model = Cliente
    success_url = reverse_lazy('cliente:cliente_listar')
    fields = ['dni', 'nombreEmpresa', 'nombreRepresentante',
              'apellidoRepresentante', 'telefono', 'correo',
              'ciudad', 'direccion', 'banco', 'tipoCuenta',
              'numeroCuenta', ]

class ClienteList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ('cliente.add_cliente')
    model = Cliente
    context_object_name = 'clientes'

class ClienteUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('cliente.change_cliente')
    model = Cliente
    success_url = reverse_lazy('cliente:cliente_listar')
    fields = ['dni', 'nombreEmpresa', 'nombreRepresentante',
              'apellidoRepresentante', 'telefono', 'correo',
              'ciudad', 'direccion', 'banco', 'tipoCuenta',
              'numeroCuenta', ]


#
# class ClienteDelete(DeleteView):
#     model = Cliente
#     success_url = reverse_lazy('cliente:cliente_listar')
#
@login_required()
@permission_required('cliente.add_cliente')
def clienteDetail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    template = loader.get_template('cliente/cliente_detail.html')
    context = {'cliente':cliente}
    return HttpResponse(template.render(context, request))
