from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from recurrencia_app.models import *
import hashlib
from urllib.request import urlopen, Request

def crear_peticion(request):
#pantalla para ingresar URL objetivo

    usuarios = Usuario.objects.all()

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
        return HttpResponse('Error. No es una URL válida')

    #creamos el objeto en la bbdd:

    Solicitud.objects.create(
        usuario = Usuario.objects.get(id=request.POST['selector_usuario']),
        url = request.POST['url_objetivo'],
        hash = hash
    )

    return HttpResponse('Solicitud ingresada correctamente')
