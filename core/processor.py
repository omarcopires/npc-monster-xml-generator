import os
from core import parser, xml_generator

def process_lua_files(folder: str, output_file: str, progress_callback) -> tuple[int, int]:
    """Processes Lua files in folder, extracts data, and generates XML."""
    npcs_data = []
    skipped_files = []

    lua_files = [os.path.join(r, f) for r, _, files in os.walk(folder) for f in files if f.endswith(".lua")]
    total_files = len(lua_files)

    for idx, file_path in enumerate(lua_files, start=1):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        name = parser.extract_npc_name(content)
        outfit = parser.extract_npc_outfit(content)

        if name and outfit and any(outfit.get(k, '0') != '0' for k in [
            'lookType', 'lookHead', 'lookBody', 'lookLegs', 'lookFeet', 'lookAddons'
        ]):
            npcs_data.append({'name': name, 'outfit': outfit})
        else:
            skipped_files.append(file_path)

        progress_callback(idx, total_files)

    xml_generator.generate_xml(npcs_data, output_file, skipped_files)
    return len(npcs_data), len(skipped_files)
