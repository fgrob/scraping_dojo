from django.urls import path
from . import views

urlpatterns = [
    path('peticion', views.crear_peticion),
    path('ingresarpeticion', views.ingresar_peticion),
]

