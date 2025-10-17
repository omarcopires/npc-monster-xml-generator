from lxml import etree

def generate_xml(npcs_data, output_file, skipped_files):
    root = etree.Element("npcs")
    npcs_data.sort(key=lambda x: x['name'])

    for npc in npcs_data:
        outfit = npc['outfit']
        attrs = {'name': npc['name']}

        if outfit.get('lookType', '0') != '0':
            attrs['looktype'] = outfit['lookType']
        if outfit.get('lookItem', '0') != '0':
            attrs['lookitem'] = outfit['lookItem']
        if outfit.get('lookAddons', '0') != '0':
            attrs['lookaddon'] = outfit['lookAddons']
        if outfit.get('lookHead', '0') != '0':
            attrs['lookhead'] = outfit['lookHead']
        if outfit.get('lookBody', '0') != '0':
            attrs['lookbody'] = outfit['lookBody']
        if outfit.get('lookLegs', '0') != '0':
            attrs['looklegs'] = outfit['lookLegs']
        if outfit.get('lookFeet', '0') != '0':
            attrs['lookfeet'] = outfit['lookFeet']

        etree.SubElement(root, "npc", **attrs)

    if skipped_files:
        skipped_elem = etree.SubElement(root, "skipped_files")
        for f in skipped_files:
            etree.SubElement(skipped_elem, "file").text = f

    tree = etree.ElementTree(root)
    with open(output_file, 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(f, encoding='utf-8', xml_declaration=False, pretty_print=True)
