"""
Brain Core

Orquestrador principal do KELLERA.
"""

from brain.voice.voice_engine import VoiceEngine
from brain.context.context_manager import ContextManager
from brain.memory.memory_manager import MemoryManager
from brain.planning.planning_agent import PlanningAgent
from brain.decision.decision_agent import DecisionAgent
from brain.actions.action_executor import ActionExecutor
from brain.narration.narration_agent import NarrationAgent


class BrainCore:

    def __init__(self):

        self.voice = VoiceEngine()
        self.context = ContextManager()
        self.memory = MemoryManager()
        self.planning = PlanningAgent()
        self.decision = DecisionAgent()
        self.executor = ActionExecutor()
        self.narration = NarrationAgent()

    def process(self, transcript: str):

        voice_result = self.voice.process_voice_input(
            transcript
        )

        if not voice_result["success"]:
            return voice_result

        intent = voice_result["intent"]

        context = self.context.get_current_context()

        plan = self.planning.create_plan(
            intent,
            context
        )

        decision = self.decision.make_decision(
            plan
        )

        action_result = self.executor.execute_action(
            decision
        )

        narration = self.narration.generate_action_response(
            action_result
        )

        return {

            "intent": intent,

            "context": context,

            "plan": plan,

            "decision": decision,

            "action": action_result,

            "narration": narration
        }
