from context_manager import ContextManager


def test_update_current_app():

    manager = ContextManager()

    manager.update_current_app("YouTube")

    context = manager.get_context()

    assert context["current_app"] == "YouTube"


def test_update_current_screen():

    manager = ContextManager()

    manager.update_current_screen("Video Screen")

    context = manager.get_context()

    assert context["current_screen"] == "Video Screen"


def test_update_last_action():

    manager = ContextManager()

    manager.update_last_action("PLAY_MEDIA")

    context = manager.get_context()

    assert context["last_action"] == "PLAY_MEDIA"


def test_update_last_user_command():

    manager = ContextManager()

    manager.update_last_user_command("Tocar música")

    context = manager.get_context()

    assert context["last_user_command"] == "Tocar música"


def test_update_last_response():

    manager = ContextManager()

    manager.update_last_response("Música iniciada.")

    context = manager.get_context()

    assert context["last_response"] == "Música iniciada."
