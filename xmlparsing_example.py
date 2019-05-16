import xml.etree.ElementTree as ET
import urllib3
tree =ET.parse(urllib3.urlopen('http://ratings.food.gov.uk/OpenDataFiles/FHRS408en-GB.xml'))
root = tree.getroot()
for child in root.iter():
   print(child.tag, child.attrib)

for child in root.find('.//EstablishmentDetail'):
    print(child.tag, child.attrib)


















#https://stackoverflow.com/questions/43921237/python-access-nested-children-in-xml-file-parsed-with-elementtree