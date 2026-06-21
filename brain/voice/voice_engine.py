"""
Voice Engine

Responsável por:

- Receber texto transcrito.
- Enviar para o IntentAnalyzer.
- Retornar a intenção detectada.
"""

from brain.intents.intent_analyzer import IntentAnalyzer


class VoiceEngine:

    def __init__(self):

        self.intent_analyzer = IntentAnalyzer()

    def process_voice_input(self, transcript: str):

        """
        Processa o texto recebido do reconhecimento de voz.
        """

        if not transcript:

            return {
                "success": False,
                "error": "Nenhuma fala detectada."
            }

        intent = self.intent_analyzer.detect_intent(
            transcript
        )

        return {
            "success": True,
            "transcript": transcript,
            "intent": intent
        }
