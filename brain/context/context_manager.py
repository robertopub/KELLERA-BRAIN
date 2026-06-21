"""
KELLERA BRAIN
Context Manager V1
"""


class ContextManager:

    def __init__(self):

        self.context = {

            "current_app": None,

            "current_screen": None,

            "last_action": None,

            "last_user_command": None,

            "last_response": None

        }

    def update_current_app(self, app_name):

        self.context["current_app"] = app_name

    def update_current_screen(self, screen):

        self.context["current_screen"] = screen

    def update_last_action(self, action):

        self.context["last_action"] = action

    def update_last_user_command(self, command):

        self.context["last_user_command"] = command

    def update_last_response(self, response):

        self.context["last_response"] = response

    def get_context(self):

        return self.context


if __name__ == "__main__":

    manager = ContextManager()

    manager.update_current_app("YouTube")

    manager.update_current_screen("Video Screen")

    manager.update_last_action("PLAY_MEDIA")

    manager.update_last_user_command("Tocar música")

    manager.update_last_response("Música iniciada.")

    print(manager.get_context())
