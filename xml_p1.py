import xml.etree.cElementTree as ET

tree = ET.parse('complex.xml')

root  = tree.getroot()

print(root.tag)

print(root.attrib)

for child in root:
	for inner in child:
		for nest in inner:
			print(nest.tag, nest.attrib, nest.text)
			if nest.tag == 'size':
				print(nest.tag)