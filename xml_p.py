import xml.etree.ElementTree as ET
import urllib3

http = urllib3.PoolManager()

response = http.request('GET', 'https://www.w3schools.com/xml/simple.xml')
#print(response.data)
#print(response.status)

cont = response.data

f = open("test.xml", "wb")
content = cont
f.write(content)
f.close()

tree = ET.parse('test.xml')
root = tree.getroot()
children = root.getchildren()

for child in children:
    ET.dump(child)
	
print(root.tag)