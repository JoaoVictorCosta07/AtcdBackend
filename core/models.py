from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    e_mail = models.CharField(max_length=200)
    whatsapp = models.CharField(max_length=11)