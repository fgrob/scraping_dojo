from django.shortcuts import render, HttpResponse
# from .tasks import waitNSeconds
from django.http import JsonResponse

# def slowResponseView(request):
#     waitNSeconds.delay(5)
#     return HttpResponse('listeilor')