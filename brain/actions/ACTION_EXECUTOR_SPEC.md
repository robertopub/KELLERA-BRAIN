# ACTION EXECUTOR SPECIFICATION V1

# Objetivo

Executar ações solicitadas pelo Planning Agent.

---

# Entrada

Plano produzido pelo Planning Agent.

Exemplo:

```json
{
    "flow": "OPEN_APP_FLOW",
    "steps": [
        "FIND_APP",
        "OPEN_APP",
        "CONFIRM_OPEN"
    ],
    "entities": {
        "app_name": "WhatsApp"
    }
}
```

---

# Responsabilidades

- Executar ações do smartphone.
- Comunicar sucesso ou falha.
- Interagir com Android Accessibility.
- Acionar APIs Android quando necessário.

---

# Ações iniciais suportadas

- FIND_APP
- OPEN_APP
- CONFIRM_OPEN
- PRESS_BACK
- GO_HOME
- OPEN_NOTIFICATIONS
- READ_NOTIFICATIONS
- ANALYZE_SCREEN
- NARRATE_SCREEN

---

# Exemplo

Entrada:

OPEN_APP

Saída:

Aplicativo aberto com sucesso.
