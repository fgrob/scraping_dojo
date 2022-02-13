from __future__ import absolute_import
from celery import shared_task
import time

@shared_task
def add(x, y):
    print('se ejecuto la funcion de sumar')
    return x + y

@shared_task
def mul(x, y):
    print('se ejecuto la funcion de multiplicar cada 2 segundos')
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def waitNSeconds(n):
    time.sleep(n)
    return ('se ejecuto parece')