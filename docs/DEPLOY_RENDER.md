# Despliegue de SIGEREC en Render

## Archivos agregados o modificados

- `sigerec/settings.py`: configuración compatible con desarrollo local y producción.
- `requirements.txt`: dependencias en UTF-8, incluyendo `gunicorn` y `whitenoise`.
- `build.sh`: script de construcción para Render.
- `Procfile`: comando de arranque con Gunicorn.
- `.python-version`: versión de Python usada para el despliegue.

## Variables de entorno recomendadas en Render

Configurar en el panel de Render:

```text
DEBUG=False
SECRET_KEY=<generar_una_clave_larga_y_segura>
ALLOWED_HOSTS=<tu-app>.onrender.com,localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=https://<tu-app>.onrender.com
```

## Build Command

```bash
./build.sh
```

## Start Command

```bash
gunicorn sigerec.wsgi:application
```

## Nota importante sobre SQLite

SIGEREC mantiene SQLite por el alcance académico del proyecto. Para una versión institucional o de uso continuo se recomienda migrar a PostgreSQL, ya que Render recomienda PostgreSQL para aplicaciones Django en producción.

## Checklist de validación posterior al despliegue

- Abrir la URL pública.
- Probar inicio de sesión.
- Registrar un reclamo.
- Consultar el reclamo por número de seguimiento.
- Entrar al dashboard.
- Exportar CSV, Excel y PDF.
- Verificar que los archivos estáticos cargan correctamente.
