# specs

Una especificación es solo para cambios grandes, como una función nueva o una migración. Las tareas pequeñas no la necesitan.

Crea una carpeta por cambio, con el mes y un título corto, por ejemplo `2026-11-sensor-ingestion/`, con tres archivos:

- `requirements.md`: lo que debe cumplirse cuando el cambio esté listo. Cada requisito empieza con un id, y se marcan los que nunca deben romperse: `R1 (critical): WHEN <condition> THE SYSTEM SHALL <behavior>` (notación EARS), o Given, When, Then. Una prueba cubre un requisito cuando lo nombra, por ejemplo `# covers 2026-11-sensor-ingestion/R1`.
- `plan.md`: cómo se va a construir y qué decisiones necesita.
- `tasks.md`: tareas pequeñas en orden, cada una con su propio criterio de terminado.

El dueño aprueba `requirements.md` antes de escribir código. Luego `python .standards/scripts/readiness.py <folder> --ci green` responde READY, NEEDS_DECISION o BLOCKED. Un requisito crítico que ninguna prueba nombra bloquea el cambio aunque el CI esté en verde.
