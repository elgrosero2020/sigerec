from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as serve_media

from vecinos.views import registro, login_view, logout_view

from reportes.views import (
    reportar,
    consultar,
    dashboard,
    cambiar_estado,
    detalle_reporte,
    exportar_reportes_csv,
    exportar_reportes_excel,
    exportar_reportes_pdf,
    centro_reportes,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='index.html'), name='inicio'),

    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('reportar/', reportar, name='reportar'),
    path('consultar/', consultar, name='consultar'),

    path('dashboard/', dashboard, name='dashboard'),
    path('cambiar_estado/<int:reporte_id>/', cambiar_estado, name='cambiar_estado'),

    # Se usa el número de seguimiento (REC-0001, REC-0002, ...)
    path(
        'reporte/<str:numero_seguimiento>/',
        detalle_reporte,
        name='detalle_reporte'
    ),

    path('reportes/', centro_reportes, name='centro_reportes'),

    path(
        'dashboard/exportar-csv/',
        exportar_reportes_csv,
        name='exportar_reportes_csv'
    ),

    path(
        'reportes/exportar-excel/',
        exportar_reportes_excel,
        name='exportar_reportes_excel'
    ),

    path(
        'reportes/exportar-pdf/',
        exportar_reportes_pdf,
        name='exportar_reportes_pdf'
    ),

    # Servicio de archivos multimedia subidos por usuarios.
    # Necesario en Render porque DEBUG=False desactiva el servicio automático de MEDIA.
    path(
        'media/<path:path>',
        serve_media,
        {'document_root': settings.MEDIA_ROOT},
        name='media'
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )