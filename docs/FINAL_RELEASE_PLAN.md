# SIGEREC — Plan de Cierre hacia v1.0.0

## Estado actual
Release Candidate estable posterior a RC1-06.

## Objetivo de v1.0.0
Entregar una versión funcional, visualmente profesional, documentada y lista para defensa académica.

## Backlog final recomendado

| ID | Tarea | Prioridad | Estado |
|----|-------|-----------|--------|
| FINAL-01 | Limpieza de `__pycache__` y `.pyc` | Alta | Pendiente |
| FINAL-02 | Manual de usuario | Alta | Pendiente |
| FINAL-03 | Manual técnico | Alta | Pendiente |
| FINAL-04 | Datos de demostración | Alta | Pendiente |
| FINAL-05 | Guion de defensa | Alta | Pendiente |
| FINAL-06 | Checklist QA final | Alta | Pendiente |
| FINAL-07 | Release Notes v1.0.0 | Media | Pendiente |
| FINAL-08 | Centro de Operaciones | Baja | Futuro v2.0 |

## Secuencia recomendada

1. Quality Pass final.
2. Crear datos de demostración.
3. Generar manuales.
4. Preparar guion de defensa.
5. Ejecutar pruebas completas.
6. Crear tag `v1.0.0`.
7. Crear ZIP final sin `venv`, `__pycache__` ni `.pyc`.

## Convención de versión final

```powershell
git add .
git commit -m "v1.0.0 release final SIGEREC"
git tag v1.0.0
```
