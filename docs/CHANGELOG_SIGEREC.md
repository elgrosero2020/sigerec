# Changelog SIGEREC

## RC1-05 — Landing Page 2.0 institucional

**Objetivo:** elevar la primera impresión del sistema y alinear la portada con el nivel visual del dashboard, centro de reportes y Design System.

**Cambios principales:**
- Nueva estructura de portada: hero institucional, proceso, indicadores reales, beneficios y CTA final.
- Indicadores dinámicos calculados desde la base de datos.
- Ilustración visual propia basada en mapa urbano, marcadores y reportes.
- Mejora de jerarquía visual, espaciado, llamadas a la acción y responsive.
- Se reemplaza la ruta de inicio basada en `TemplateView` por una vista `inicio` con contexto dinámico.

**Archivos modificados:**
- `templates/index.html`
- `reportes/views.py`
- `sigerec/urls.py`
- `static/css/sigerec-ui.css`


## v1.3.2 — Design System inicial

### Agregado
- Carpeta `templates/components/` para componentes reutilizables.
- Componente `page_hero.html` para encabezados institucionales compactos.
- Componente `empty_state.html` para pantallas sin datos.
- Componente `status_badge.html` para estados visuales unificados.
- Componente `section_card.html` como base para futuras tarjetas institucionales.

### Mejorado
- Se agregaron clases CSS base en `templates/base.html` bajo el bloque `SIGEREC UI v1.3.2`.
- El Centro de Reportes comienza a usar el nuevo componente de encabezado.
- La vista previa sin resultados en Reportes ahora usa un estado vacío profesional.

### Nota técnica
Esta versión no toca modelos, base de datos, migraciones ni lógica crítica. Es una base de arquitectura visual para que las próximas pantallas compartan la misma identidad.

## RC1-02 — Estados vacíos elegantes

**Objetivo:** mejorar la experiencia cuando no existen datos para mostrar o cuando los filtros no devuelven resultados.

**Cambios:**
- Se reemplazaron mensajes vacíos simples por componentes institucionales.
- Se mejoró el estado vacío del Dashboard del Presidente.
- Se mejoró el estado vacío del Dashboard del Vecino.
- Se ajustó el mensaje del Centro de Reportes cuando no hay datos para exportar.

**Archivos modificados:**
- `templates/dashboard_presidente.html`
- `templates/dashboard_vecino.html`
- `templates/centro_reportes.html`
- `docs/CHANGELOG_SIGEREC.md`


## RC1-04 — Polish UX inicial

**Objetivo:** mejorar la sensación de producto terminado mediante microinteracciones y retroalimentación visual.

**Cambios:**
- Loader institucional con mensajes dinámicos según la acción ejecutada.
- Botones de formularios se bloquean visualmente durante el envío para evitar doble clic.
- Exportaciones CSV/Excel muestran estado de generación mientras se prepara la descarga.
- Se agregaron microanimaciones suaves en tarjetas y filas de tablas.
- Se reforzaron estados `hover`, `focus` y `active` de botones y campos.

**Archivos modificados:**
- `templates/base.html`
- `templates/centro_reportes.html`
- `templates/dashboard_presidente.html`
- `docs/CHANGELOG_SIGEREC.md`

**Riesgo:** bajo. No modifica modelos, migraciones ni base de datos.
## RC1-06 — PDF Institucional Premium

- Se agrega exportación PDF desde el Centro de Reportes.
- El PDF respeta filtros activos del módulo de reportes.
- Incluye encabezado institucional, datos del informe, resumen ejecutivo, tabla de reclamos y pie de página.
- Se agrega ReportLab como dependencia del proyecto.

Archivos modificados:
- reportes/views.py
- sigerec/urls.py
- templates/centro_reportes.html
- requirements.txt

