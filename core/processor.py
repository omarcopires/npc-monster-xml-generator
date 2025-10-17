import os
from . import npc_parser
from . import monster_parser

def process_files(folder: str, output_file: str, progress_callback, type_: str = "npc") -> tuple[int,int]:
    """
    Process Lua files to extract NPCs or Monsters and generate XML.
    :param folder: folder with Lua files
    :param output_file: path to save XML
    :param progress_callback: function(current, total) for progress updates
    :param type_: "npc" or "monster"
    :return: tuple(success_count, skipped_count)
    """
    data = []
    skipped_files = []

    lua_files = [os.path.join(r, f) for r, _, files in os.walk(folder) for f in files if f.endswith(".lua")]
    total = len(lua_files)

    for idx, file_path in enumerate(lua_files, start=1):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if type_ == "npc":
            name = npc_parser.extract_npc_name(content)
            outfit = npc_parser.extract_npc_outfit(content)
            keys = ['lookType','lookHead','lookBody','lookLegs','lookFeet','lookAddons']
        elif type_ == "monster":
            name = monster_parser.extract_monster_name(content)
            outfit = monster_parser.extract_monster_outfit(content)
            keys = ['lookTypeEx','lookType','lookHead','lookBody','lookLegs','lookFeet','lookAddons']
        else:
            raise ValueError("Unknown type. Must be 'npc' or 'monster'.")

        if name and outfit and any(outfit.get(k,'0') != '0' for k in keys):
            data.append({'name':name,'outfit':outfit})
        else:
            skipped_files.append(file_path)

        progress_callback(idx, total)

    # Generate XML
    if type_ == "npc":
        from . import xml_generator
        xml_generator.generate_xml(data, output_file, skipped_files)
    else:
        monster_parser.generate_xml(data, output_file, skipped_files)

    return len(data), len(skipped_files)
