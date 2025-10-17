import re

def extract_npc_name(content: str) -> str | None:
    """Extracts the NPC name from Lua content."""
    match = re.search(r'local\s+internalNpcName\s*=\s*"(.+?)"', content)
    return match.group(1) if match else None

def extract_npc_outfit(content: str) -> dict | None:
    """Extracts the NPC outfit dictionary from Lua content."""
    match = re.search(r'npcConfig\.outfit\s*=\s*\{([^}]+)\}', content, re.DOTALL)
    if not match:
        return None
    return dict(re.findall(r'(\w+)\s*=\s*(\d+)', match.group(1)))

# Future placeholder for monster parsing
def extract_monster_name(content: str) -> str | None:
    return None

def extract_monster_outfit(content: str) -> dict | None:
    return None
