from django.db import models

class User(models.Model):
    user = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #solicitudes -- recurrencia_app
    #logs -- recurrencia_app

    def __str__(self):
        return f"{self.user}"
    def __repr__(self):
        return f"{self.user}"