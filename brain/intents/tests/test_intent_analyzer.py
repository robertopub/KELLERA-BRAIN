from intent_analyzer import IntentAnalyzer


def test_open_app():

    analyzer = IntentAnalyzer()

    result = analyzer.analyze("Abra o WhatsApp")

    assert result["intent"] == "OPEN_APP"
    assert result["entities"]["app_name"] == "whatsapp"


def test_go_back():

    analyzer = IntentAnalyzer()

    result = analyzer.analyze("Voltar")

    assert result["intent"] == "GO_BACK"


def test_notifications():

    analyzer = IntentAnalyzer()

    result = analyzer.analyze("Leia minhas notificações")

    assert result["intent"] == "READ_NOTIFICATIONS"
