from lxml import etree

def generate_xml(npcs_data: list, output_file: str, skipped_files: list):
    """Generates an XML file from NPC or monster data."""
    root = etree.Element("npcs")
    for npc in sorted(npcs_data, key=lambda x: x['name']):
        outfit = npc['outfit']
        attrs = {'name': npc['name']}
        for k, v in {
            'lookType': 'looktype',
            'lookItem': 'lookitem',
            'lookAddons': 'lookaddon',
            'lookHead': 'lookhead',
            'lookBody': 'lookbody',
            'lookLegs': 'looklegs',
            'lookFeet': 'lookfeet'
        }.items():
            if outfit.get(k, '0') != '0':
                attrs[v] = outfit[k]
        etree.SubElement(root, "npc", **attrs)

    if skipped_files:
        skipped_elem = etree.SubElement(root, "skipped_files")
        for f in skipped_files:
            etree.SubElement(skipped_elem, "file").text = f

    xml_bytes = etree.tostring(root, encoding="utf-8", pretty_print=True, xml_declaration=True)
    xml_text = xml_bytes.decode("utf-8").replace("  ", "\t")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(xml_text)
