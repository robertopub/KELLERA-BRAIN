"""
KELLERA BRAIN
Memory Manager V1
"""


class MemoryManager:

    def __init__(self):

        self.memory = {}

    def save_memory(self, key, value):

        self.memory[key] = value

    def get_memory(self, key):

        return self.memory.get(key)

    def update_memory(self, key, value):

        self.memory[key] = value

    def delete_memory(self, key):

        if key in self.memory:

            del self.memory[key]

    def get_all_memories(self):

        return self.memory


if __name__ == "__main__":

    manager = MemoryManager()

    manager.save_memory("user_name", "Roberto")

    manager.save_memory("favorite_app", "YouTube")

    print(manager.get_all_memories())
