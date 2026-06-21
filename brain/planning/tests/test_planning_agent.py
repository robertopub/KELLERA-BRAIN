from planning_agent import PlanningAgent


def test_open_app_plan():

    agent = PlanningAgent()

    input_data = {

        "selected_flow": "OPEN_APP_FLOW",

        "entities": {

            "app_name": "WhatsApp"

        }

    }

    result = agent.create_plan(input_data)

    assert result["flow"] == "OPEN_APP_FLOW"

    assert result["steps"] == [

        "FIND_APP",

        "OPEN_APP",

        "CONFIRM_OPEN"

    ]


def test_back_plan():

    agent = PlanningAgent()

    input_data = {

        "selected_flow": "BACK_FLOW"

    }

    result = agent.create_plan(input_data)

    assert result["steps"] == [

        "PRESS_BACK"

    ]


def test_unknown_plan():

    agent = PlanningAgent()

    input_data = {

        "selected_flow": "SOMETHING_UNKNOWN"

    }

    result = agent.create_plan(input_data)

    assert result["steps"] == [

        "UNKNOWN_ACTION"

    ]
