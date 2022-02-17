from django.shortcuts import render, redirect
from django.contrib import messages
from mailing_app.models import User
import bcrypt
from mailing_app.email import send_user_mail
from recurrencia_app.models import Solicitud


def registro(request):
    if request.method == 'GET':

        if 'user' in request.session:
            messages.warning(request,"Ya estás registrado.")
            return redirect("/")

        context = {}
        return render(request, 'registro.html', context)

    if request.method == 'POST':
        pass_encriptada = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            user = request.POST['user'],
            email = request.POST['email'],
            password = pass_encriptada,
        )

        user_session = {
            'id' : user.id,
            'user' : user.user,
            'email' : user.email
        }

        request.session['user'] = user_session

        messages.success(request, "Usuario creado exitosamente.")
        return redirect("/")


def login(request):
    if request.method == 'GET':

        if 'user' in request.session:
            messages.warning(request,"Ya estás logeado.")
            return redirect("/")

        context = {}
        return render(request, 'login.html', context)

    if request.method == 'POST':

        users = User.objects.filter(user=request.POST['user']) 
        if users: 
            user = users[0] 

            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):

                user_session = {
                    'id' : user.id,
                    'user' : user.user,
                    'email' : user.email
                }

                request.session['user'] = user_session
                messages.success(request, "Logeado Correctamente")
                return redirect('/')
            else:
                messages.error(request, "La contraseña o el correo NO COINCIDE")
                return redirect("/login/")
        else:
            messages.error(request,"El correo o la contraseña indicado no EXISTE")
            return redirect("/login/")

def index(request):

    if 'user' not in request.session:
        messages.error(request,"NO estas logeado.")
        return redirect("/login/")

    user = User.objects.get(id=request.session['user']['id'])
    context = {
        'user':user
    }

    return render(request, 'index.html', context)        
        

def logout(request):
    if 'user' in request.session:
        del request.session['user']

    return redirect("/login/")


def logs(request, solicitud_id):

    solicitud = Solicitud.objects.get(id=solicitud_id)

    context = {
        'solicitud': solicitud
    }
   
    solicitud.status = '0'
    solicitud.save()

    return render(request, 'log.html', context)
