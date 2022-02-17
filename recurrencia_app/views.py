from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import *
import hashlib
from urllib.request import urlopen, Request

#mailing app:
from mailing_app.email import send_user_mail


def ingresar_peticion(request):
#procesar y guardar la info en la BBDD
   
    #hasheamos el website:
    try:
        url = Request(request.POST['url_objetivo'])
        response = urlopen(url).read()
        hash = hashlib.sha224(response).hexdigest()
    except:
        messages.error(request, "URL inválida")
        return redirect('/')

    #creamos el objeto en la bbdd:

    Solicitud.objects.create(
        user = User.objects.get(id=request.session['user']['id']),
        url = request.POST['url_objetivo'],
        hash = hash
    )

    messages.success(request, "URL Ingresada")
    return redirect('/')
