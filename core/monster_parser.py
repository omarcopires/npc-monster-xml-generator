import re
from lxml import etree

def extract_monster_name(content):
    match = re.search(r'local mType\s*=\s*Game\.createMonsterType\("(.+?)"\)', content)
    return match.group(1) if match else None

def extract_monster_outfit(content):
    match = re.search(r'monster\.outfit\s*=\s*\{([^}]+)\}', content, re.DOTALL)
    if not match:
        return None

    outfit = {}
    for line in match.group(1).splitlines():
        kv = re.search(r'(\w+)\s*=\s*(\d+)', line)
        if kv:
            outfit[kv.group(1)] = kv.group(2)
    return outfit

def generate_xml(monsters_data, output_file, skipped_files):
    root = etree.Element("monsters")
    monsters_data.sort(key=lambda x: x['name'])

    for monster in monsters_data:
        outfit = monster['outfit']
        attrs = {'name': monster['name']}

        if outfit.get('lookTypeEx', '0') != '0':
            attrs['lookitem'] = outfit['lookTypeEx']
        elif any(outfit.get(k, '0') != '0' for k in ['lookType','lookHead','lookBody','lookLegs','lookFeet','lookAddons']):
            attrs.update({
                'looktype': outfit.get('lookType', '0'),
                'lookhead': outfit.get('lookHead', '0'),
                'lookbody': outfit.get('lookBody', '0'),
                'looklegs': outfit.get('lookLegs', '0'),
                'lookfeet': outfit.get('lookFeet', '0'),
                'lookaddons': outfit.get('lookAddons', '0')
            })
            attrs = {k: v for k, v in attrs.items() if v != '0' or k=='looktype'}
        elif 'lookType' in outfit:
            attrs['looktype'] = outfit['lookType']

        etree.SubElement(root, "monster", **attrs)

    if skipped_files:
        skipped_elem = etree.SubElement(root, "skipped_files")
        for f in skipped_files:
            etree.SubElement(skipped_elem, "file").text = f

    tree = etree.ElementTree(root)
    with open(output_file, 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(f, encoding='utf-8', xml_declaration=False, pretty_print=True)
