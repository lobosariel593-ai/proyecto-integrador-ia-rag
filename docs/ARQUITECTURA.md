# Arquitectura objetivo (propuesta, no sistema validado)

```text
Web / mensajería simulada
        |
Orquestador y control de sesión
        |--------------------------> Solicitud de humano (handoff)
Clasificación de intención
        |
Recuperador documental <--- Corpus autorizado, versionado, con doc_id y fecha
        |
Validación de evidencia y permisos
        |--- evidencia insuficiente ---> Abstención + agente
Modelo generativo (LLM) + contexto recuperado
        |
Verificación de citas, políticas y seguridad
        |
Respuesta con fuente + registro mínimo de auditoría
```

**Controles:** minimización de PII, acceso por rol, no registrar credenciales, defensa frente a instrucciones incrustadas en documentos, revisión de vigencia de precios/políticas, confirmación humana para operaciones sensibles. **No afirmar** que la empresa aprobó acceso a pedidos o bases internas.

**Despliegue académico:** iniciar con web y un canal de mensajería simulado; ampliaciones a WhatsApp/correo/CRM solo con autorización y recursos disponibles.
