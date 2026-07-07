# Changelog SIGEREC

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
