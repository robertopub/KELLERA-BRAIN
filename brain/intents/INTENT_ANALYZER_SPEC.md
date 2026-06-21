# INTENT ANALYZER SPECIFICATION V1

# Objetivo

Identificar a intenção do usuário a partir de comandos de voz.

---

# Entrada

Texto proveniente do Voice Agent.

Exemplos:

"Abra o WhatsApp."

"Volte."

"Leia minhas notificações."

---

# Saída

Objeto estruturado contendo:

- Intent.
- Entidades.
- Confiança.

Exemplo:

```json
{
    "intent": "OPEN_APP",
    "entities": {
        "app_name": "WhatsApp"
    },
    "confidence": 0.98
}
```

---

# Fluxo

Usuário fala
↓
Voice Agent converte voz em texto
↓
Intent Analyzer recebe texto
↓
Intent Analyzer identifica intenção
↓
Intent Analyzer extrai entidades
↓
Intent Analyzer retorna resultado

---

# Intents suportadas inicialmente

- OPEN_APP
- GO_HOME
- GO_BACK
- READ_NOTIFICATIONS
- READ_SCREEN
- SEARCH_CONTENT
- PLAY_MEDIA
- PAUSE_MEDIA

---

# Exemplo 1

Entrada:

"Abrir YouTube"

Saída:

Intent: OPEN_APP

Entidade:

YouTube

---

# Exemplo 2

Entrada:

"Voltar"

Saída:

Intent: GO_BACK

---

# Exemplo 3

Entrada:

"Leia minhas notificações"

Saída:

Intent: READ_NOTIFICATIONS
