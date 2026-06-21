# DECISION AGENT SPECIFICATION V1

# Objetivo

Decidir qual fluxo deverá ser executado com base na intenção identificada.

---

# Entrada

Resultado proveniente do Intent Analyzer.

Exemplo:

```json
{
    "intent": "OPEN_APP",
    "entities": {
        "app_name": "WhatsApp"
    },
    "confidence": 0.95
}
```

---

# Responsabilidades

- Validar a intenção.
- Escolher o fluxo adequado.
- Encaminhar para o Planning Agent.

---

# Fluxos iniciais

OPEN_APP
→ Open App Flow

GO_BACK
→ Back Flow

GO_HOME
→ Home Flow

READ_NOTIFICATIONS
→ Notification Flow

READ_SCREEN
→ Screen Reading Flow

---

# Exemplo

Entrada:

OPEN_APP

Saída:

Executar fluxo Open App Flow.
