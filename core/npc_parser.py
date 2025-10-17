import re

def extract_npc_name(content):
    match = re.search(r'local internalNpcName\s*=\s*"(.+?)"', content)
    return match.group(1) if match else None

def extract_npc_outfit(content):
    match = re.search(r'npcConfig\.outfit\s*=\s*\{([^}]+)\}', content, re.DOTALL)
    if not match:
        return None

    outfit = {}
    for line in match.group(1).splitlines():
        kv = re.search(r'(\w+)\s*=\s*(\d+)', line)
        if kv:
            outfit[kv.group(1)] = kv.group(2)
    return outfit
