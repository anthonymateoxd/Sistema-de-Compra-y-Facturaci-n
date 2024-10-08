from django.db import models
from django.contrib.auth.models import User

class ClaseModelo(models.Model):  # Corregido 'codels.Model' a 'models.Model'

    estado = models.BooleanField(default=True)  # 'True' en mayúscula
    fc = models.DateTimeField(auto_now_add=True)  # 'True' en mayúscula
    fm = models.DateTimeField(auto_now=True)  # 'True' en mayúscula
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)  # 'True' en mayúscula

    class Meta:
        abstract = True  # 'True' en mayúscula
