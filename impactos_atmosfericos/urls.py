
from django.urls import path
from impactos_atmosfericos.views import*
from .import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('listaap', views.listaap, name='listaap'),
    path('crearAp/', views.crearAp, name='crearAp'),
    path('edicionAp/<int:id>', views.edicionAp, name='edicionAp'),
    path('editarAp/', views.editarAp, name='editarAp'),
    path('eliminarAp/<int:id>', views.eliminarAp, name='eliminarAp'),
    path('displayAp', views.displayAp, name='displayAp'),
    path('crearTiempo/', views.crearTiempo, name='crearTiempo'),
    path('listaTime', views.listaTime, name='listaTime'),
    path('edicionTime/<int:id>', views.edicionTime, name='edicionTime'),
    path('editarTime/', views.editarTime, name='editarTime'),
    path('eliminarTime/<int:id>', views.eliminarTime, name='eliminarTime'),
    path('listapocp', views.listaPocp, name='listaPocp'),
    path('crearPocp/', views.crearPocp, name='crearPocp'),
    path('edicionPocp/<int:id>', views.edicionPocp, name='edicionPocp'),
    path('editarPocp/', views.editarPocp, name='editarPocp'),
    path('eliminarPocp/<int:id>', views.eliminarPocp, name='eliminarPocp'),
    path('displayPocp', views.displayPocp, name='displayPocp'),
    path('crearOdp/', views.crearOdp, name='crearOdp'),
    path('edicionOdp/<int:id>', views.edicionOdp, name='edicionOdp'),
    path('editarOdp/', views.editarOdp, name='editarOdp'),
    path('listaOdp', views.listaOdp, name='listaOdp'),
    path('eliminarOdp/<int:id>', views.eliminarOdp, name='eliminarOdp'),
    path('displayOdp', views.displayOdp, name='displayOdp'),
    path('crearGwp/', views.crearGwp, name='crearGwp'),
    path('listaGwp', views.listaGwp, name='listaGwp'),
    path('editarGwp/', views.editarGwp, name='editarGwp'),
    path('edicionGwp/<int:id>', views.edicionGwp, name='edicionGwp'),
    path('eliminarGwp/<int:id>', views.eliminarGwp, name='eliminarGwp'),
    
]