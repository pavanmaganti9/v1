import xml.etree.cElementTree as ET

tree = ET.parse('dummy.xml')

root  = tree.getroot()

print(root.tag)

print(root.attrib)

for child in root:
    print(child.tag, child.attrib)
    #print(len(root))
    if child.attrib=='Liechtenstein':
        print(child.text)

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    year = country.find('year').text
    gdppc = country.find('gdppc').text
    print(name, rank, year, gdppc)