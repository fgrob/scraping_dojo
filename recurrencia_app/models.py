from django.db import models
import hashlib
from urllib.request import urlopen, Request
from mailing_app.models import User

class Solicitud(models.Model):

    STATUS_SOLICITUD = (
        ('0', 'Sin cambios detectados'),
        ('1', 'Se detectaron cambios'),
    )

    user = models.ForeignKey(User, related_name="solicitudes", on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=500)
    hash = models.CharField(max_length=256)
    status = models.CharField(max_length=1, choices=STATUS_SOLICITUD, default='0')
    #logs

    created_at = models.DateTimeField(auto_now_add=True)
 
class Log(models.Model):
    solicitud = models.ForeignKey(Solicitud, related_name="logs", on_delete=models.CASCADE)
    status_log = models.CharField(max_length=50)
    ruta_img = models.CharField(max_length=60, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    
