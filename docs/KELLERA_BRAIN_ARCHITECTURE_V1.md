# KELLERA BRAIN ARCHITECTURE V1

# Objetivo

O KELLERA BRAIN é responsável por coordenar todos os agentes do ecossistema KELLERA.

---

# Arquitetura Geral

Usuário
↓
Voice Agent
↓
Intent Analyzer
↓
Decision Agent
↓
Planning Agent
↓
Action Executor
↓
Accessibility Layer
↓
Smartphone

---

# Agentes

## Voice Agent

Responsabilidades:

- Escutar o usuário.
- Converter voz em texto.
- Falar com o usuário.

Entrada:

Voz.

Saída:

Texto.

---

## Intent Analyzer

Responsabilidades:

- Identificar a intenção do usuário.

Exemplo:

"Abra o WhatsApp."

↓

OPEN_APP

---

## Decision Agent

Responsabilidades:

- Decidir o que deve ser feito.
- Escolher o fluxo adequado.

---

## Planning Agent

Responsabilidades:

- Criar uma sequência de ações.

Exemplo:

Objetivo:

Abrir WhatsApp.

Plano:

1. Localizar aplicativo.
2. Abrir aplicativo.
3. Confirmar abertura.

---

## Action Executor

Responsabilidades:

- Executar o plano.

Exemplos:

- Clicar.
- Abrir aplicativo.
- Rolar tela.
- Voltar.

---

## Context Agent

Responsabilidades:

- Descobrir onde o usuário está.
- Identificar aplicativo atual.
- Identificar tela atual.

---

## Narration Agent

Responsabilidades:

- Explicar continuamente o contexto ao usuário.

Exemplo:

"Você está no YouTube."

"Há cinco vídeos recomendados."

---

## Memory Agent

Responsabilidades:

- Armazenar contexto.
- Histórico.
- Preferências.
- Conversas anteriores.

---

# Ciclo Principal

ESCUTAR
↓
ENTENDER
↓
DECIDIR
↓
PLANEJAR
↓
EXECUTAR
↓
DESCOBRIR CONTEXTO
↓
NARRAR
↓
ESCUTAR NOVAMENTE
