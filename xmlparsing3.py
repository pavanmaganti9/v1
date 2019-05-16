import xml.etree.cElementTree as ElementTree

tree = ElementTree.parse('cefixime.xml')
root = tree.getroot()

for node in tree.findall('.//stuff'):
    for sn in node.getchildren():
        print(sn.tag, sn.text)

for child in root:
    print(child.tag)
for node in tree.findall('.//section'):
    for snode in node.getchildren():
        print(snode.tag, snode.text)