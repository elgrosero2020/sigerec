from django.db import models
from vecinos.models import Vecino

class Reporte(models.Model):
    TIPOS = (
        ('bache', 'Bache'),
        ('basura', 'Basura acumulada'),
        ('alumbrado', 'Alumbrado dañado'),
        ('otro', 'Otro'),
    )

    ESTADOS = (
        ('reportado', 'Reportado'),
        ('validado', 'Validado por junta'),
        ('derivado', 'Derivado al municipio'),
        ('proceso', 'En proceso'),
        ('resuelto', 'Resuelto'),
    )

    vecino = models.ForeignKey(Vecino, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    latitud = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    foto = models.ImageField(upload_to='reportes/', null=True, blank=True)
    numero_seguimiento = models.CharField(max_length=20, unique=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='reportado')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.numero_seguimiento} - {self.tipo}"

    @property
    def tiene_gps(self):
        return self.latitud is not None and self.longitud is not None

    @property
    def google_maps_url(self):
        if self.tiene_gps:
            return f"https://www.google.com/maps?q={self.latitud},{self.longitud}"
        return ""

    class Meta:
        verbose_name_plural = "Reportes"


class Historial(models.Model):
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE)
    estado_anterior = models.CharField(max_length=20)
    estado_nuevo = models.CharField(max_length=20)
    fecha_cambio = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(blank=True)

    def __str__(self):
        return f"{self.reporte.numero_seguimiento} - {self.estado_anterior} → {self.estado_nuevo}"

    class Meta:
        verbose_name_plural = "Historiales"