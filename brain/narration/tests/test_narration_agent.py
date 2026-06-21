"""
Tests for NarrationAgent
"""

import unittest

from brain.narration.narration_agent import NarrationAgent


class TestNarrationAgent(unittest.TestCase):

    def setUp(self):

        self.agent = NarrationAgent()

    def test_generate_context_response_complete(self):

        context = {

            "current_app": "YouTube",

            "current_screen": "Vídeo reproduzindo"

        }

        response = self.agent.generate_context_response(context)

        self.assertEqual(

            response,

            "Você está no YouTube. Tela atual: Vídeo reproduzindo."

        )

    def test_generate_context_response_only_app(self):

        context = {

            "current_app": "WhatsApp"

        }

        response = self.agent.generate_context_response(context)

        self.assertEqual(

            response,

            "Você está no aplicativo WhatsApp."

        )

    def test_generate_context_response_unknown(self):

        response = self.agent.generate_context_response({})

        self.assertEqual(

            response,

            "Não foi possível identificar o contexto atual."

        )

    def test_generate_action_response(self):

        response = self.agent.generate_action_response(

            "OPEN_APP"

        )

        self.assertEqual(

            response,

            "Aplicativo aberto com sucesso."

        )

    def test_generate_navigation_response(self):

        response = self.agent.generate_navigation_response(

            "Configurações"

        )

        self.assertEqual(

            response,

            "Navegando para Configurações."

        )


if __name__ == "__main__":

    unittest.main()
