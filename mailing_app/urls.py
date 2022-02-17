from django.urls import path
from . import views
urlpatterns = [
    path('registro/', views.registro),
    path('login/', views.login), 
    path('', views.index),  
    path('logout/', views.logout),
    path('log/<int:solicitud_id>', views.logs),
]

