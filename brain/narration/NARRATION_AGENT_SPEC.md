# NARRATION AGENT SPECIFICATION V1

# Objetivo

Transformar contexto interno do KELLERA em respostas naturais para o usuário.

---

# Responsabilidades

- Informar contexto atual.
- Explicar ações realizadas.
- Narrar telas.
- Guiar o usuário.
- Produzir respostas conversacionais.

---

# Exemplo

Entrada:

{
    "current_app": "YouTube",
    "current_screen": "Vídeo reproduzindo"
}

Saída:

"Você está no YouTube. Um vídeo está sendo reproduzido."

---

# Funções principais

generate_context_response()

generate_action_response()

generate_navigation_response()
