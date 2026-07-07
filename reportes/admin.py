from django.contrib import admin
from .models import Reporte, Historial

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('numero_seguimiento', 'vecino', 'tipo', 'estado', 'ubicacion', 'fecha_creacion')
    list_filter = ('tipo', 'estado', 'fecha_creacion')
    search_fields = ('numero_seguimiento', 'vecino__nombre', 'ubicacion', 'descripcion')
    readonly_fields = ('numero_seguimiento', 'fecha_creacion', 'fecha_actualizacion')
    ordering = ('-fecha_creacion',)

@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ('reporte', 'estado_anterior', 'estado_nuevo', 'fecha_cambio')
    list_filter = ('estado_nuevo', 'fecha_cambio')
    search_fields = ('reporte__numero_seguimiento',)
    readonly_fields = ('fecha_cambio',)
    ordering = ('-fecha_cambio',)
