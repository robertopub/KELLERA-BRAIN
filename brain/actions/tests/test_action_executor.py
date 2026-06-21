from action_executor import ActionExecutor


def test_open_app_execution():

    executor = ActionExecutor()

    plan = {

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

    result = executor.execute(plan)

    assert len(result) == 3

    assert result[0] == "Searching app: WhatsApp"

    assert result[1] == "Opening app: WhatsApp"

    assert result[2] == "Application opened successfully."


def test_back_execution():

    executor = ActionExecutor()

    plan = {

        "flow": "BACK_FLOW",

        "steps": [

            "PRESS_BACK"

        ]

    }

    result = executor.execute(plan)

    assert result[0] == "Pressed BACK."


def test_unknown_execution():

    executor = ActionExecutor()

    plan = {

        "flow": "UNKNOWN_FLOW",

        "steps": [

            "INVALID_ACTION"

        ]

    }

    result = executor.execute(plan)

    assert "Unknown action" in result[0]
