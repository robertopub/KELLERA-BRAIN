"""
KELLERA BRAIN
Decision Agent V1
"""


class DecisionAgent:

    def decide(self, intent_result: dict) -> dict:

        intent = intent_result.get("intent")

        flow_map = {

            "OPEN_APP": "OPEN_APP_FLOW",

            "GO_BACK": "BACK_FLOW",

            "GO_HOME": "HOME_FLOW",

            "READ_NOTIFICATIONS": "NOTIFICATION_FLOW",

            "READ_SCREEN": "SCREEN_READING_FLOW",

            "SEARCH_CONTENT": "SEARCH_FLOW",

            "PLAY_MEDIA": "MEDIA_PLAY_FLOW",

            "PAUSE_MEDIA": "MEDIA_PAUSE_FLOW"

        }

        selected_flow = flow_map.get(
            intent,
            "UNKNOWN_FLOW"
        )

        return {

            "intent": intent,

            "selected_flow": selected_flow,

            "entities": intent_result.get("entities", {}),

            "confidence": intent_result.get("confidence", 0.0)

        }


if __name__ == "__main__":

    agent = DecisionAgent()

    example = {

        "intent": "OPEN_APP",

        "entities": {

            "app_name": "WhatsApp"

        },

        "confidence": 0.95
    }

    result = agent.decide(example)

    print(result)
