# KELLERA USER JOURNEY V1

# Cenário 1 - Desbloqueio do Celular

## Evento

O usuário desbloqueia o smartphone.

---

## Objetivo do KELLERA

Assumir imediatamente a interação e informar o contexto atual ao usuário.

---

## Fluxo

1. Detectar que o celular foi desbloqueado.

2. Assumir o controle da interação.

3. Identificar o aplicativo atual.

4. Identificar a tela atual.

5. Verificar hora e data.

6. Verificar notificações importantes.

7. Montar um resumo do contexto.

8. Informar o contexto ao usuário.

9. Entrar em modo de escuta.

---

## Exemplo de interação

KELLERA:

"Celular desbloqueado."

"Você está na tela inicial."

"São nove horas e quinze minutos."

"Há duas notificações não lidas."

"O que deseja fazer agora?"

---

## Estado Final

KELLERA permanece aguardando comandos do usuário.

# Cenário 2 - Abrir um Aplicativo

## Exemplo

Usuário:

"Abra o WhatsApp."

---

## Objetivo do KELLERA

Permitir que o usuário abra qualquer aplicativo utilizando apenas voz.

---

## Fluxo

1. Escutar o comando do usuário.

2. Converter voz em texto.

3. Identificar a intenção:

   Intent: OPEN_APP

4. Identificar qual aplicativo foi solicitado.

   App: WhatsApp

5. Verificar se o aplicativo está instalado.

6. Abrir o aplicativo.

7. Confirmar que o aplicativo foi aberto.

8. Identificar a tela atual.

9. Informar o contexto ao usuário.

10. Entrar novamente em modo de escuta.

---

## Exemplo de interação

Usuário:

"Abra o WhatsApp."

KELLERA:

"Abrindo WhatsApp."

"WhatsApp aberto."

"Você está na lista de conversas."

"Há três mensagens não lidas."

"O que deseja fazer agora?"

---

## Estado Final

KELLERA permanece aguardando novos comandos.
