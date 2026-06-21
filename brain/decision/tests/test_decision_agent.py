from decision_agent import DecisionAgent


def test_open_app_flow():

    agent = DecisionAgent()

    input_data = {

        "intent": "OPEN_APP",

        "entities": {

            "app_name": "WhatsApp"

        },

        "confidence": 0.95
    }

    result = agent.decide(input_data)

    assert result["selected_flow"] == "OPEN_APP_FLOW"


def test_go_back_flow():

    agent = DecisionAgent()

    input_data = {

        "intent": "GO_BACK",

        "entities": {},

        "confidence": 0.99
    }

    result = agent.decide(input_data)

    assert result["selected_flow"] == "BACK_FLOW"


def test_unknown_flow():

    agent = DecisionAgent()

    input_data = {

        "intent": "SOMETHING_UNKNOWN",

        "entities": {},

        "confidence": 0.10
    }

    result = agent.decide(input_data)

    assert result["selected_flow"] == "UNKNOWN_FLOW"
