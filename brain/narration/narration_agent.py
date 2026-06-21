"""
KELLERA BRAIN
Narration Agent V1
"""


class NarrationAgent:

    def generate_context_response(self, context):

        app = context.get("current_app")

        screen = context.get("current_screen")

        if app and screen:

            return f"Você está no {app}. Tela atual: {screen}."

        elif app:

            return f"Você está no aplicativo {app}."

        return "Não foi possível identificar o contexto atual."

    def generate_action_response(self, action):

        responses = {

            "OPEN_APP": "Aplicativo aberto com sucesso.",

            "GO_HOME": "Você retornou para a tela inicial.",

            "PRESS_BACK": "Voltando para a tela anterior.",

            "READ_NOTIFICATIONS": "Lendo notificações.",

            "PLAY_MEDIA": "Reprodução iniciada.",

            "PAUSE_MEDIA": "Reprodução pausada."

        }

        return responses.get(

            action,

            "Ação executada."

        )

    def generate_navigation_response(self, destination):

        return f"Navegando para {destination}."


if __name__ == "__main__":

    agent = NarrationAgent()

    example = {

        "current_app": "YouTube",

        "current_screen": "Vídeo reproduzindo"

    }

    print(agent.generate_context_response(example))
