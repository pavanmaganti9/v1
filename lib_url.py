import urllib
from urllib import request
var = dir(request)

resp = request.urlopen("https://stackoverflow.com/questions/39975367/attributeerror-module-urllib-has-no-attribute-urlopen/39975383")

print(resp.code)

print(resp.length)

print(resp.peek())

data = resp.read()

print(type(data))

html = data.decode("UTF-8")

print(type(html))

print(html)