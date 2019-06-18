from xml.dom import minidom
xmldoc = minidom.parse('cefixime.xml')
itemlist = xmldoc.getElementsByTagName('component')
print(len(itemlist))

roo = itemlist[0]

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

staffs = roo.getElementsByTagName("title")
for staff in staffs:
	#sid = staff.getAttribute("id")
    nickname = staff.getElementsByTagName("title")
    #salary = staff.getElementsByTagName("salary")[0]
    print(getNodeText(staff))