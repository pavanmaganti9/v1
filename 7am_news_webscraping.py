import urllib.request
from bs4 import BeautifulSoup
from csv import writer
response = urllib.request.urlopen('https://www.ap7am.com/telugu-flash-news.html')

data = response.read()
#print(data)

soup = BeautifulSoup(data,'html.parser')
#print(soup.body)

links = soup.find_all('a')
#print(links.gettext)

#for link in soup.find_all('a'):
    #print(link.get_text())

el = soup.find(class_="titlelist").get_text()

#print(el)

with open('posts.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title']
    csv_writer.writerow(headers)

    for item in soup.select(".titlelist"):
        title1 = item.get_text()
        print(title1)
        #csv_writer.writerow([title1])