import urllib.request
from bs4 import BeautifulSoup
from csv import writer
response = urllib.request.urlopen('https://simpleisbetterthancomplex.com/')

data = response.read()
#print(data)
soup = BeautifulSoup(data,'html.parser')
#print(soup.body)
#print(soup.head)
#print(soup.head.title.text)

#el = soup.find('div')

#el = soup.find_all('div')

#el = soup.find_all('div')[0]

#el = soup.find(class_="post-title").get_text()

for item in soup.select(".post-title"):
    print(item.get_text())

el = soup.body.contents
print(el)