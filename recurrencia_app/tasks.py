from __future__ import absolute_import

from celery import shared_task
from .models import *
from time import sleep
import hashlib
from urllib.request import urlopen, Request
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
            continue
        else:          
            print('-------------------------------------------------------------------------')
            print('URL OBJETIVO:',url)
            print('**HAY CAMBIOS EN LA WEB!**')
            print('-------------------------------------------------------------------------')
            solicitud.hash = hash
            solicitud.save()

            #screenshots:
            options = Options()
            options.headless = True
            driver = webdriver.Chrome('recurrencia_app/webdriver/chromedriver.exe', chrome_options=options)
            driver.maximize_window()
            driver.get(url)
            now = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
            driver.save_screenshot("screenshots/screenshot-%s.png" % now)
            driver.close()

                      

