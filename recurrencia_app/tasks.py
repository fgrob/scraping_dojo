from __future__ import absolute_import

from celery import shared_task
from .models import *
from time import sleep
import hashlib
from urllib.request import urlopen, Request
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from mailing_app.email import send_user_mail

@shared_task
def add():

    for solicitud in Solicitud.objects.all():
        url = solicitud.url
        response = urlopen(url).read()

        #recorremos cada palabra. Si la palabra es muy larga, la quitamos. El objetivo es quitar los tokens variables que afectarían el hashing
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

            Log.objects.create(
                solicitud = solicitud,
                status_log = solicitud.get_status_display(),
                ruta_img = '',                
            )

            continue
        else:
            #actualizamos la BBDD:
            solicitud.hash = hash
            solicitud.status = '1'
            solicitud.save()

            now = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
            ruta = "static/screenshots/screenshot-%s.png" % now

            Log.objects.create(
                solicitud = solicitud,
                status_log = solicitud.get_status_display(),
                ruta_img = ruta,                
            )

            print('-------------------------------------------------------------------------')
            print('URL OBJETIVO:',url)
            print('**HAY CAMBIOS EN LA WEB!**')
            print('-------------------------------------------------------------------------')

            #screenshots:
            options = Options()
            options.headless = True
            driver = webdriver.Chrome('recurrencia_app/webdriver/chromedriver.exe', chrome_options=options)
            driver.maximize_window()
            driver.get(url)
            s = driver.get_window_size() # pedimos las medidas
            w = driver.execute_script('return document.body.parentNode.scrollWidth')
            h = driver.execute_script('return document.body.parentNode.scrollHeight')
            driver.set_window_size(w, h)
                        
            driver.save_screenshot("recurrencia_app/" + ruta)
            driver.close()            

            #enviamos correo avisando
            send_user_mail(solicitud)

                      

