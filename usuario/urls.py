# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    #url(r'^login/$', views.authentication, name="authentication"),
    url(r'^$', views.authentication, name="authentication"),
    url(r'^plataforma', views.systemIndex, name="system_index"),
    url(r'^perfil/new', views.PerfilInsert.as_view(), name="perfil_insert"),
    url(r'^perfil/list$',views.PerfilList.as_view(), name='perfil_list'),
    url(r'^perfil/edit(?P<pk>[0-9]+)/$',views.PerfilUpdate.as_view(),
    	name='perfil_edit'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name="logout"),

    url(r'^pagina_quienesSomos', views.paginaquienesSomos, name='pagina_quienesSomos'),
    url(r'^pagina_Cubiertos', views.paginaCubiertos, name='pagina_Cubiertos'),
    url(r'^pagina_Bolsas', views.paginaBolsas, name='pagina_Bolsas'),
    url(r'^pagina_ProInstitucional', views.paginaProInstitucional,
        name='pagina_ProInstitucional'),
    url(r'^pagina_Pinateria', views.paginaPinateria, name='pagina_Pinateria'),
    url(r'^pagina_LagunaFuquene', views.paginaLagunaFuquene,
        name='pagina_LagunaFuquene'),
    url(r'^pagina_FloresGuavata', views.paginaFloresGuavata,
        name='pagina_FloresGuavata'),
    url(r'^pagina_Cooperativismo', views.paginaCooperativismo,
        name='pagina_Cooperativismo'),

]
