"""
KELLERA BRAIN
Intent Analyzer V1
"""

import re


class IntentAnalyzer:

    def analyze(self, text: str) -> dict:

        text = text.lower().strip()

        # OPEN APP

        open_patterns = [
            r"abra (o|a)?\s*(.+)",
            r"abrir (o|a)?\s*(.+)",
            r"quero abrir (o|a)?\s*(.+)"
        ]

        for pattern in open_patterns:

            match = re.match(pattern, text)

            if match:

                app_name = match.group(2).strip()

                return {
                    "intent": "OPEN_APP",
                    "entities": {
                        "app_name": app_name
                    },
                    "confidence": 0.95
                }

        # GO BACK

        if text in ["voltar", "volte", "tela anterior"]:
            return {
                "intent": "GO_BACK",
                "entities": {},
                "confidence": 0.99
            }

        # GO HOME

        if text in [
            "ir para tela inicial",
            "voltar para tela inicial",
            "ir para home",
            "home"
        ]:
            return {
                "intent": "GO_HOME",
                "entities": {},
                "confidence": 0.99
            }

        # READ NOTIFICATIONS

        if "notificação" in text or "notificações" in text:
            return {
                "intent": "READ_NOTIFICATIONS",
                "entities": {},
                "confidence": 0.95
            }

        # FALLBACK

        return {
            "intent": "UNKNOWN",
            "entities": {},
            "confidence": 0.0
        }


if __name__ == "__main__":

    analyzer = IntentAnalyzer()

    examples = [
        "Abra o WhatsApp",
        "Voltar",
        "Leia minhas notificações",
        "Abra o YouTube"
    ]

    for phrase in examples:

        result = analyzer.analyze(phrase)

        print("\nEntrada:", phrase)
        print("Resultado:", result)
