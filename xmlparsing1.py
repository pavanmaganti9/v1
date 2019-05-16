import xml.etree.ElementTree as ET
tree = ET.parse('cefixime.xml')
root = tree.getroot()
#children = root.getchildren()
#print(root.tag)

#for child in children:
    #ET.dump(child)
    #print(child.tag)
    #if child.tag == 'effectiveTime':
     #   print('yes')



#for element in tree.iter():
	#print(element.tag)
	#print(element.text)

for node in tree.findall('section'):
    for snode in node.getchildren():
        print(snode)

item = root.find("title")
print(item)