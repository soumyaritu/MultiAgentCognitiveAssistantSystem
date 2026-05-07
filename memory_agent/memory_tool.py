memory_store = []


def save_memory(note: str) -> str:
    """Save a memory note."""
    memory_store.append(note)
    return "✅ Memory saved"


def get_memory() -> str:
    """Retrieve all stored memories."""
    if not memory_store:
        return "No stored memories"
    return "\n".join(memory_store)
