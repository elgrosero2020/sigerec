# SIGEREC — Architecture

## 1. Introducción

SIGEREC es un sistema web desarrollado con Django para registrar, consultar y gestionar reclamos ciudadanos en un contexto vecinal. Su primera versión está orientada a un barrio piloto de Trinidad, Beni, Bolivia.

El sistema permite que los vecinos registren reclamos urbanos y que el presidente de la junta vecinal realice seguimiento, cambio de estados, consulta de historial y exportación de información.

## 2. Objetivo arquitectónico

El objetivo de la arquitectura actual es mantener un sistema simple, funcional y extensible, adecuado para un MVP académico con posibilidad de evolucionar a una plataforma institucional.

## 3. Tecnologías principales

- Python.
- Django.
- SQLite.
- HTML.
- CSS.
- JavaScript.
- Bootstrap.
- Leaflet / OpenStreetMap.
- OpenPyXL.
- Pillow.

## 4. Estructura general del proyecto

```text
sigerec/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── sigerec/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── vecinos/
│   ├── models.py
│   ├── forms.py
│   └── views.py
├── reportes/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── migrations/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── reportar.html
│   ├── consultar.html
│   ├── dashboard_presidente.html
│   ├── dashboard_vecino.html
│   ├── centro_reportes.html
│   └── components/
├── static/
│   ├── css/
│   └── images/
├── media/
└── docs/
```

## 5. Aplicaciones Django

### vecinos

Gestiona la información del vecino y su relación con el usuario autenticado de Django.

Responsabilidades:

- Registro de vecinos.
- Autenticación con CI como usuario.
- Roles de usuario: vecino y presidente.
- Datos personales básicos.

### reportes

Gestiona el núcleo funcional del sistema.

Responsabilidades:

- Registro de reclamos.
- Gestión de estados.
- Historial de cambios.
- GPS.
- Consulta pública.
- Dashboards.
- Centro de reportes.
- Exportaciones.

## 6. Modelo de datos

### Vecino

Representa a una persona registrada en el sistema.

Campos principales:

- nombre.
- ci.
- direccion.
- telefono.
- barrio.
- rol.
- usuario.
- fecha_registro.

Relación:

- Un vecino se asocia con un usuario de Django mediante relación uno a uno.

### Reporte

Representa un reclamo ciudadano.

Campos principales:

- vecino.
- tipo.
- descripcion.
- ubicacion.
- latitud.
- longitud.
- foto.
- numero_seguimiento.
- estado.
- fecha_creacion.
- fecha_actualizacion.

Relación:

- Un vecino puede tener muchos reportes.

### Historial

Representa cada cambio de estado realizado sobre un reclamo.

Campos principales:

- reporte.
- estado_anterior.
- estado_nuevo.
- fecha_cambio.
- comentario.

Relación:

- Un reporte puede tener muchos registros históricos.

## 7. Flujo principal del ciudadano

```text
Inicio
  ↓
Registro / Login
  ↓
Reportar reclamo
  ↓
Capturar ubicación GPS opcional
  ↓
Adjuntar evidencia opcional
  ↓
Generar número de seguimiento
  ↓
Consultar estado
```

## 8. Flujo principal del presidente

```text
Login
  ↓
Dashboard Presidente
  ↓
Revisar reclamos del barrio
  ↓
Filtrar / priorizar
  ↓
Cambiar estado
  ↓
Registrar historial
  ↓
Exportar información desde Centro de Reportes
```

## 9. Estados del reclamo

- Reportado.
- Validado por junta.
- Derivado al municipio.
- En proceso.
- Resuelto.

Estos estados permiten representar el avance del reclamo desde su registro inicial hasta su cierre.

## 10. GPS y mapas

El sistema usa la API de geolocalización del navegador para capturar latitud y longitud.

Características:

- No requiere API externa para capturar coordenadas.
- Funciona en localhost y sitios con HTTPS.
- Genera enlace a Google Maps.
- Muestra mapas embebidos mediante Leaflet / OpenStreetMap.

## 11. Exportaciones

### CSV

Permite descarga rápida de datos tabulares. Usa separador compatible con Excel en español.

### Excel institucional

Genera un archivo `.xlsx` con estructura profesional mediante OpenPyXL.

Incluye:

- Resumen ejecutivo.
- Filtros aplicados.
- Tabla de reportes.
- Datos GPS.
- Enlaces a Google Maps.

## 12. Design System

SIGEREC incluye una base visual reutilizable ubicada en:

```text
templates/components/
static/css/sigerec-ui.css
```

Objetivo:

- Mantener coherencia visual.
- Reducir repetición.
- Facilitar futuras pantallas.
- Dar identidad institucional al sistema.

## 13. Riesgos actuales

### SQLite

Es adecuado para desarrollo y demostración, pero no para producción institucional con alto volumen.

Mitigación futura:

- Migrar a PostgreSQL.

### Archivos multimedia

Actualmente las imágenes se guardan localmente en `media/`.

Mitigación futura:

- Usar almacenamiento externo o configuración robusta en producción.

### Roles limitados

La versión actual contempla vecino y presidente.

Mitigación futura:

- Agregar administrador municipal, operador y supervisor.

## 14. Decisiones arquitectónicas relevantes

### Django monolítico

Se eligió Django por rapidez de desarrollo, estructura clara y soporte integrado para modelos, vistas, formularios y autenticación.

### SQLite

Se eligió por simplicidad para una primera versión académica y facilidad de instalación.

### GPS progresivo

Se implementó primero captura simple de coordenadas, luego enlaces y mapas embebidos. Esto redujo riesgos y permitió validar la utilidad antes de agregar complejidad.

### Centro de Reportes separado

Se separó del dashboard para evitar saturar la pantalla operativa y preparar futuras exportaciones y análisis.

## 15. Futuras mejoras arquitectónicas

- Separar vistas en módulos por responsabilidad.
- Crear servicios para exportaciones.
- Migrar a PostgreSQL.
- Implementar API REST.
- Crear panel administrativo institucional.
- Implementar notificaciones.
- Agregar auditoría avanzada.
- Preparar despliegue en servidor con HTTPS.
