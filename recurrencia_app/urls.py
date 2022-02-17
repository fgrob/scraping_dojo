from django.urls import path
from . import views

urlpatterns = [
    path('ingresarpeticion', views.ingresar_peticion),
]

