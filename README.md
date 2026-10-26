# Proyecto Integrador UEES — Asistente omnicanal con IA generativa y RAG

**Autores:** Luis Sebastián Arias Loaiza y Cristian Paúl Quintana Velásquez.  
**Docente:** Gladys Villegas.  
**Universidad:** Universidad de Especialidades Espíritu Santo (UEES).

## Alcance
Prototipo académico para consultas de ventas y posventa de una tienda tecnológica de referencia. **No es una integración oficial con iShop Ecuador**, ni accede a clientes, inventario, pedidos o CRM reales. El código adjunto es un **baseline local de recuperación léxica**, no una implementación productiva de LLM/RAG; la arquitectura RAG prevista está documentada en `docs/ARQUITECTURA.md`.

## Contenido
- `src/retrieval_baseline.py`: recuperación lexical explicable con biblioteca estándar.
- `tests/test_retrieval.py`: pruebas unitarias de recuperación y abstención.
- `data/consultas_sinteticas.csv`: muestras ficticias, no datos personales reales.
- `data/base_conocimiento_demo.json`: documentos ilustrativos **no oficiales**, con referencias a políticas hipotéticas.
- `docs/ARQUITECTURA.md`: flujo propuesto RAG, protección de datos y derivación humana.
- `docs/EVALUACION.md`: protocolo de KPIs, denominadores y separación de experimentos.
- `docs/DATOS_Y_LICENCIAS.md`: fuentes candidatas y validaciones de licencia pendientes.
- `docs/MOCKUP.md`: esquema textual de la interfaz.

## Ejecución (Python 3.10+, sin dependencias externas)
```bash
python -m unittest discover -s tests -v
python src/retrieval_baseline.py "¿Qué hago si necesito una garantía?"
```

## Estado y limitaciones
La implementación local demuestra recuperación simple y una regla de abstención. **No demuestra** cumplimiento de KPIs de RAG, fidelidad de un LLM, omnicanalidad efectiva ni derivación a un agente real. Para ello se necesita completar la integración y ejecutar el protocolo de evaluación.

## Publicación en GitHub
1. Crear repositorio privado inicialmente (p. ej. `uees-proyecto-integrador-rag`).
2. Subir estos archivos sin credenciales ni conversaciones reales.
3. Verificar README, archivos y licencia antes de hacerlo público.
4. Adjuntar la URL del repositorio en la plataforma académica, si dispone de campo o como anexo.

## Derechos
El código de ejemplo se ofrece con licencia MIT (`LICENSE`). Las fuentes de datos externas conservan sus respectivas licencias; no se redistribuyen aquí. El uso del nombre iShop es exclusivamente contextual y no implica patrocinio.
