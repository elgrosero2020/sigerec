from django.contrib import admin
from .models import Vecino

@admin.register(Vecino)
class VecinoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ci', 'telefono', 'barrio', 'rol', 'fecha_registro')
    list_filter = ('barrio', 'rol')
    search_fields = ('nombre', 'ci', 'telefono')
    ordering = ('-fecha_registro',)