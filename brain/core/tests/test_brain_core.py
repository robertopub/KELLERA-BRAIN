"""
Tests for BrainCore
"""

import unittest

from brain.core.brain_core import BrainCore


class TestBrainCore(unittest.TestCase):

    def setUp(self):

        self.core = BrainCore()

    def test_process_valid_command(self):

        result = self.core.process(
            "Abrir WhatsApp"
        )

        self.assertEqual(
            result["intent"],
            "OPEN_APP"
        )

        self.assertIn(
            "decision",
            result
        )

        self.assertIn(
            "action",
            result
        )

        self.assertIn(
            "narration",
            result
        )

    def test_process_empty_command(self):

        result = self.core.process("")

        self.assertFalse(
            result["success"]
        )

        self.assertEqual(
            result["error"],
            "Nenhuma fala detectada."
        )


if __name__ == "__main__":

    unittest.main()
