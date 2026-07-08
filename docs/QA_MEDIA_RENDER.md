# QA Media en Render

## Problema corregido
En producción `DEBUG=False`, por lo que Django no sirve automáticamente los archivos cargados por usuarios en `MEDIA_URL`. Esto hacía que las fotografías adjuntas a los reportes no se visualizaran aunque estuvieran guardadas.

## Solución aplicada
Se agregó una ruta explícita para servir archivos multimedia desde `MEDIA_ROOT`:

```python
path('media/<path:path>', serve_media, {'document_root': settings.MEDIA_ROOT}, name='media')
```

## Nota técnica
Esta solución es suficiente para la demostración académica y las capturas del informe. Para una versión institucional se recomienda migrar las imágenes a un almacenamiento externo como Cloudinary, S3 o similar, porque el almacenamiento local de Render puede no persistir después de reinicios o nuevos despliegues.
