import urllib.request
from bs4 import BeautifulSoup
from csv import writer
response = urllib.request.urlopen('https://simpleisbetterthancomplex.com/')

data = response.read()
print(data)
#soup = BeautifulSoup(data,'html.parser')