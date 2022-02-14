from __future__ import absolute_import

from celery import shared_task
from .models import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
import hashlib
from urllib.request import urlopen, Request
from datetime import datetime


@shared_task
def add():
    options = Options()
    options.headless = True
    website = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    website.maximize_window() # maximizamos para sacar un pantallazo completo
    website.set_page_load_timeout(5)

    for solicitud in Solicitud.objects.all():
        try:                
            print(solicitud.url)
            website.get(solicitud.url)
            s = website.get_window_size() # pedimos las medidas
            w = website.execute_script('return document.body.parentNode.scrollWidth')
            h = website.execute_script('return document.body.parentNode.scrollHeight')
            website.set_window_size(w, h)
            sleep(1)
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            website.find_element_by_tag_name('body').screenshot("screenshots/screenshot-%s.png" % now)   
            website.quit()
            print("finalizando...")
        except:
            website.delete_all_cookies()
            print('Falló la conexión con ', solicitud.url)
            return

#version final con verificación de hash
# @shared_task
# def add():
#     options = Options()
#     options.headless = True
#     website = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
#     website.maximize_window() # maximizamos para sacar un pantallazo completo

#     for solicitud in Solicitud.objects.all():
#         url = solicitud.url
#         response = urlopen(url).read()
#         hash = hashlib.sha224(response).hexdigest()
#         if hash == solicitud.hash:
#             continue
#         else:          
#             website.get(solicitud.url)
#             s = website.get_window_size() # pedimos las medidas
#             w = website.execute_script('return document.body.parentNode.scrollWidth')
#             h = website.execute_script('return document.body.parentNode.scrollHeight')
#             website.set_window_size(w, h)
#             sleep(1)
#             now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            # website.find_element_by_tag_name('body').screenshot("screenshots/screenshot-%s.png" % now)   
#             website.quit()
#             print("finalizando...")
#     pass



#version original
# @shared_task
# def add():
#     options = Options()
#     options.headless = True
#     website = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
#     website.maximize_window() # maximizamos para sacar un pantallazo completo   
#     website.get('https://www.galpondediseno.cl/products/tabla-redonda-madera-negra')
#     s = website.get_window_size() # pedimos las medidas
#     w = website.execute_script('return document.body.parentNode.scrollWidth')
#     h = website.execute_script('return document.body.parentNode.scrollHeight')
#     website.set_window_size(w, h)
#     sleep(1)
#     website.find_element_by_tag_name('body').screenshot("screenshots/pantallazo.png")   
#     website.quit()
#     print("finalizando...")

#     pass

