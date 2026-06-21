"""
KELLERA BRAIN
Planning Agent V1
"""


class PlanningAgent:

    def create_plan(self, decision_result: dict) -> dict:

        selected_flow = decision_result.get("selected_flow")

        flow_plans = {

            "OPEN_APP_FLOW": [

                "FIND_APP",
                "OPEN_APP",
                "CONFIRM_OPEN"

            ],

            "BACK_FLOW": [

                "PRESS_BACK"

            ],

            "HOME_FLOW": [

                "GO_HOME"

            ],

            "NOTIFICATION_FLOW": [

                "OPEN_NOTIFICATIONS",
                "READ_NOTIFICATIONS"

            ],

            "SCREEN_READING_FLOW": [

                "ANALYZE_SCREEN",
                "NARRATE_SCREEN"

            ],

            "SEARCH_FLOW": [

                "SEARCH_CONTENT"

            ],

            "MEDIA_PLAY_FLOW": [

                "PLAY_MEDIA"

            ],

            "MEDIA_PAUSE_FLOW": [

                "PAUSE_MEDIA"

            ]

        }

        steps = flow_plans.get(

            selected_flow,

            ["UNKNOWN_ACTION"]

        )

        return {

            "flow": selected_flow,

            "steps": steps,

            "entities": decision_result.get("entities", {})

        }


if __name__ == "__main__":

    agent = PlanningAgent()

    example = {

        "intent": "OPEN_APP",

        "selected_flow": "OPEN_APP_FLOW",

        "entities": {

            "app_name": "WhatsApp"

        },

        "confidence": 0.95

    }

    result = agent.create_plan(example)

    print(result)
