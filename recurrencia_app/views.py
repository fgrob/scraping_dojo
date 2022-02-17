from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import *
import hashlib
from urllib.request import urlopen, Request

#mailing app:
from mailing_app.email import send_user_mail

def crear_peticion(request):
#pantalla para ingresar URL objetivo

    usuarios = User.objects.all()

    context = {'usuarios' : usuarios}

    return render(request, 'crear_peticion.html', context)


def ingresar_peticion(request):
#procesar y guardar la info en la BBDD

    print(request.POST)
    
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

#-----------BORRAR:
def enviar_correo(request):
    
    send_user_mail(User.objects.get(id=1))
    
    return HttpResponse('correo enviado')