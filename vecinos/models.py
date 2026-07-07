from django.db import models
from django.contrib.auth.models import User

class Vecino(models.Model):
    ROLES = (
        ('vecino', 'Vecino'),
        ('presidente', 'Presidente de Junta Vecinal'),
    )

    nombre = models.CharField(max_length=100)
    ci = models.CharField(max_length=15, unique=True)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    barrio = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROLES, default='vecino')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.rol}"

    class Meta:
        verbose_name_plural = "Vecinos"