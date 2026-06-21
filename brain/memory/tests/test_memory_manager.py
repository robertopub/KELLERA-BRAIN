from memory_manager import MemoryManager


def test_save_memory():

    manager = MemoryManager()

    manager.save_memory("user_name", "Roberto")

    assert manager.get_memory("user_name") == "Roberto"


def test_update_memory():

    manager = MemoryManager()

    manager.save_memory("favorite_app", "YouTube")

    manager.update_memory("favorite_app", "Spotify")

    assert manager.get_memory("favorite_app") == "Spotify"


def test_delete_memory():

    manager = MemoryManager()

    manager.save_memory("temp", "value")

    manager.delete_memory("temp")

    assert manager.get_memory("temp") is None


def test_get_all_memories():

    manager = MemoryManager()

    manager.save_memory("name", "Roberto")

    manager.save_memory("language", "Português")

    memories = manager.get_all_memories()

    assert memories["name"] == "Roberto"

    assert memories["language"] == "Português"
