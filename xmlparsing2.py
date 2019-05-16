import xml.etree.ElementTree as ET
import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://ratings.food.gov.uk/OpenDataFiles/FHRS408en-GB.xml')
response = r.data
tree = ET.parse(response)
root  = tree.getroot()
#root = response.getroot()
#for child in root.iter():
    #print(child.tag, child.attrib)

for child in root.find('.//EstablishmentDetail'):
    print(child.tag)
    print()