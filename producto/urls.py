#-*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^new', views.ProductoInsert.as_view(),
		name="producto_insert"),
	url(r'^list$', views.ProductoList.as_view(),
		name='producto_list'),
	url(r'^edit(?P<pk>[0-9]+)/$', views.ProductoUpdate.as_view(),
    	name='producto_edit'),
	#  url(r'^inventario/delete(?P<pk>[0-9]+)/$', views.InventarioDelete.as_view(),
	#  	name="inventario_delete"),
	url(r'^(?P<pk>[0-9]+)/$', views.producto_detail,
		name="producto_detail"),
]
