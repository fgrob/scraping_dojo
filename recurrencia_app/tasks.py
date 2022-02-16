from __future__ import absolute_import

from celery import shared_task
from .models import *
from time import sleep
import hashlib
from urllib.request import urlopen, Request
from datetime import datetime

@shared_task
def add():

    for solicitud in Solicitud.objects.all():
        url = solicitud.url
        response = urlopen(url).read()

        #recorremos cada palabra. Si es muy larga, la quitamos. Esto es para evitar los tokens variables que afectarían el hashing
        for word in response.split():
            if len(word) > 40:
                empty = ''
                response = response.replace(word, empty.encode())
                
        hash = hashlib.sha224(response).hexdigest()

        if hash == solicitud.hash:
            print('-------------------------------------------------------------------------')
            print('URL OBJETIVO: ',url)
            print('**Sin cambios**')
            print('-------------------------------------------------------------------------')

            continue
        else:          
            print('-------------------------------------------------------------------------')
            print('URL OBJETIVO:',url)
            print('**HAY CAMBIOS EN LA WEB!**')
            print('-------------------------------------------------------------------------')
            solicitud.hash = hash
            solicitud.save()

