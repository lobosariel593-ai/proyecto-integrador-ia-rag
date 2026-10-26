# Protocolo de evaluación (metas, no resultados)

1. Congelar corpus, versión de prompts, modelos, índices y preguntas de evaluación.
2. Construir 200 escenarios sintéticos o de fuente pública, con al menos 40 de posventa, 40 comerciales, 40 multi-turno, 40 sin evidencia y 40 de seguridad/escalamiento. No utilizar consultas reales sin consentimiento y autorización.
3. Anotar relevancia documental y respuesta de referencia con dos revisores; resolver desacuerdos.
4. Medir **Recall@5** = consultas con documento relevante en top 5 / consultas con documento relevante conocido; excluir o informar aparte preguntas sin evidencia.
5. Medir **faithfulness** = respuestas sustentadas / respuestas evaluables, con rúbrica y doble revisión; reportar intervalos de confianza cuando corresponda.
6. Medir **abstención correcta** = abstenciones adecuadas / consultas sin evidencia; **handoff** = escalaciones correctas / escenarios que requieren humano.
7. Medir latencia p50/p95, fallas, costos por consulta, satisfacción (encuesta voluntaria) y resolución; declarar denominadores.
8. Comparar baseline léxico, LLM sin RAG (si existe) y RAG, con mismas preguntas y criterios. No extrapolar resultados de clasificación de intención de Semana 3 a calidad del sistema RAG.
9. Documentar fallos, sesgos de español ecuatoriano y casos de información obsoleta.
