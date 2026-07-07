from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from vecinos.views import registro, login_view, logout_view
from reportes.views import inicio, reportar, consultar, dashboard, cambiar_estado, detalle_reporte, exportar_reportes_csv, centro_reportes, exportar_reportes_excel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('reportar/', reportar, name='reportar'),
    path('consultar/', consultar, name='consultar'),
    path('reporte/<str:numero_seguimiento>/', detalle_reporte, name='detalle_reporte'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/exportar-csv/', exportar_reportes_csv, name='exportar_reportes_csv'),
    path('reportes/', centro_reportes, name='centro_reportes'),
    path('reportes/exportar-excel/', exportar_reportes_excel, name='exportar_reportes_excel'),
    path('cambiar_estado/<int:reporte_id>/', cambiar_estado, name='cambiar_estado'),
    
]

# Configuración para servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)