# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
#from recursos import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^new', views.ClienteInsert.as_view(),
		name= "cliente_insert"),
	url(r'^list$', views.ClienteList.as_view(),
		name='cliente_list'),
    url(r'^cliente/update(?P<pk>[0-9]+)/$', views.ClienteUpdate.as_view(),
        name='cliente_update'),
    url(r'^cliente/detail(?P<pk>[0-9]+)/$', views.clienteDetail,
        name='cliente_detalle'),
	# url(r'^cliente/delete(?P<pk>[0-9]+)/$', views.ClienteDelete.as_view(),
	#  	name="cliente_delete"),
	# url(r'^(?P<pk>[0-9]+)/$', views.cliente_detail,
	# 	name="cliente_detail"),
]
