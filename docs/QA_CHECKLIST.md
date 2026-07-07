# SIGEREC — QA Checklist

## 1. Pruebas generales

- [ ] El servidor inicia sin errores.
- [ ] La página de inicio carga correctamente.
- [ ] La navegación funciona en todas las secciones.
- [ ] El diseño mantiene coherencia visual.
- [ ] No aparecen errores en consola del navegador.

## 2. Registro e inicio de sesión

- [ ] Un vecino puede registrarse.
- [ ] El CI se usa correctamente como usuario.
- [ ] El login funciona con credenciales válidas.
- [ ] El sistema rechaza credenciales incorrectas.
- [ ] El logout redirige correctamente.

## 3. Reportar reclamo

- [ ] El formulario carga correctamente.
- [ ] Los campos obligatorios validan correctamente.
- [ ] El botón GPS solicita permiso al navegador.
- [ ] Latitud y longitud se guardan si el usuario acepta.
- [ ] El reporte puede enviarse sin foto.
- [ ] El reporte puede enviarse con foto.
- [ ] Se genera número de seguimiento.
- [ ] El usuario llega al detalle o confirmación del reclamo.

## 4. Consulta pública

- [ ] Se puede consultar un código existente.
- [ ] Si el código no existe, se muestra mensaje claro.
- [ ] Se muestra estado actual.
- [ ] Se muestra historial.
- [ ] Se muestra evidencia si existe.
- [ ] Se muestra mapa si existe GPS.
- [ ] El enlace a Google Maps funciona.

## 5. Dashboard vecino

- [ ] Solo muestra reportes del vecino autenticado.
- [ ] Los contadores coinciden con sus reportes.
- [ ] Los botones de detalle funcionan.
- [ ] Los mapas cargan si hay GPS.
- [ ] La tabla no se rompe si no hay reportes.

## 6. Dashboard presidente

- [ ] Solo muestra reportes del barrio correspondiente.
- [ ] Filtros por estado funcionan.
- [ ] Filtros por tipo funcionan.
- [ ] Búsqueda funciona.
- [ ] Filtro GPS funciona.
- [ ] Cambio de estado guarda correctamente.
- [ ] El historial se actualiza.
- [ ] El modal funciona correctamente.

## 7. Centro de Reportes

- [ ] La pantalla carga correctamente.
- [ ] Exportación CSV funciona.
- [ ] Exportación Excel funciona.
- [ ] Los filtros se respetan en exportaciones.
- [ ] El archivo descargado abre correctamente en Excel.

## 8. Accesibilidad básica

- [ ] Los textos son legibles.
- [ ] Los botones tienen tamaño suficiente.
- [ ] Los colores tienen contraste aceptable.
- [ ] Los formularios tienen etiquetas claras.
- [ ] El usuario entiende los mensajes de error.

## 9. Defensa / demostración

- [ ] Existe usuario vecino para prueba.
- [ ] Existe usuario presidente para prueba.
- [ ] Existen reportes con GPS.
- [ ] Existen reportes con foto.
- [ ] Existen reportes en diferentes estados.
- [ ] La exportación Excel tiene datos suficientes.
- [ ] La demo puede hacerse sin crear datos desde cero.
