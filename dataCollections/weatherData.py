import requests


apiKey = "06a29a351dba490fe9b5a24faa87e578"
url = "http://api.openweathermap.org/data/2.5/weather?zip=08054,us&APPID={}".format(apiKey)
print url
response = requests.get(url)


print response.json()
