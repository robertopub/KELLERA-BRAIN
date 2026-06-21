"""
KELLERA BRAIN
Action Executor V1
"""


class ActionExecutor:

    def execute(self, plan: dict):

        steps = plan.get("steps", [])

        results = []

        for step in steps:

            result = self._execute_step(step, plan)

            results.append(result)

        return results

    def _execute_step(self, step: str, plan: dict):

        entities = plan.get("entities", {})

        if step == "FIND_APP":

            app = entities.get("app_name")

            return f"Searching app: {app}"

        elif step == "OPEN_APP":

            app = entities.get("app_name")

            return f"Opening app: {app}"

        elif step == "CONFIRM_OPEN":

            return "Application opened successfully."

        elif step == "PRESS_BACK":

            return "Pressed BACK."

        elif step == "GO_HOME":

            return "Navigated to HOME."

        elif step == "OPEN_NOTIFICATIONS":

            return "Notifications panel opened."

        elif step == "READ_NOTIFICATIONS":

            return "Reading notifications."

        elif step == "ANALYZE_SCREEN":

            return "Analyzing current screen."

        elif step == "NARRATE_SCREEN":

            return "Narrating screen."

        else:

            return f"Unknown action: {step}"


if __name__ == "__main__":

    executor = ActionExecutor()

    example_plan = {

        "flow": "OPEN_APP_FLOW",

        "steps": [

            "FIND_APP",

            "OPEN_APP",

            "CONFIRM_OPEN"

        ],

        "entities": {

            "app_name": "WhatsApp"

        }

    }

    result = executor.execute(example_plan)

    print(result)
