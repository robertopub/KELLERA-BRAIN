"""
Tests for VoiceEngine
"""

import unittest

from brain.voice.voice_engine import VoiceEngine


class TestVoiceEngine(unittest.TestCase):

    def setUp(self):

        self.engine = VoiceEngine()

    def test_process_valid_voice(self):

        result = self.engine.process_voice_input(
            "Abrir WhatsApp"
        )

        self.assertTrue(result["success"])

        self.assertEqual(
            result["transcript"],
            "Abrir WhatsApp"
        )

        self.assertEqual(
            result["intent"],
            "OPEN_APP"
        )

    def test_process_empty_voice(self):

        result = self.engine.process_voice_input(
            ""
        )

        self.assertFalse(result["success"])

        self.assertEqual(
            result["error"],
            "Nenhuma fala detectada."
        )


if __name__ == "__main__":

    unittest.main()
