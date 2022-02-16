from django.db import models
import hashlib
from urllib.request import urlopen, Request

class Usuario(models.Model):
    usuario = models.CharField(max_length=50)
    correo = models.EmailField(max_length=200)
    #solicitudes

    

class Solicitud(models.Model):
    usuario = models.ForeignKey(Usuario, related_name="solicitudes", on_delete=models.SET_NULL, blank=True, null=True)
    url = models.CharField(max_length=500)
    hash = models.CharField(max_length=256)
    respuesta_read = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
 

    
