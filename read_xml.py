import xml.etree.ElementTree as ET
tree = ET.parse('cefixime.xml')
root = tree.getroot()

print(root.attrib)

# for child in root:
	# print(child.tag, child.attrib)
	
print(root[7])

pr = ET.tostring(root[7]).decode()
#print(pr)
#root2 = ET.parse(pr).getroot()

# for type_tag in root2.findall('component'):
    # value = type_tag.get('structuredBody')
    # print(value)
	
#inn = root2.findall('component')
from xml.dom import minidom
xmldoc = minidom.parse('cefixime.xml')
itemlist = xmldoc.getElementsByTagName('component')
print(len(itemlist))
print(itemlist[0])
roo = itemlist[0]
print(roo)
print(roo.nodeName)
print(roo.firstChild)

#title = xmldoc.getElementsByTagName("title")
#print(title.length)
#print(title.nodeName("title"))

def getNodeText(node):
    nodelist = node.childNodes
    result = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)

name = roo.getElementsByTagName("title")[0]
print("Node Name : %s" % name.nodeName)
print("Node Value : %s \n" % getNodeText(name))
# for s in itemlist:
    # print(s.attributes['title'].value)
	
staffs = roo.getElementsByTagName("paragraph")
for staff in staffs:
	#sid = staff.getAttribute("id")
    nickname = staff.getElementsByTagName("title")
    #salary = staff.getElementsByTagName("salary")[0]
    print(getNodeText(staff))