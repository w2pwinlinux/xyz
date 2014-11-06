import httplib
connection = httplib.HTTPConnection("www.rubenbernardez.com")
connection.request("GET","/blog/")
response = connection.getresponse()
data = response.read()
connection.close()