import requests

API_URL = "api.openweathermap.org/data/2.5/weather"
KEY = "28641f35c9c547ab0665ac5e3c8e339b"

Parameters = {
    "q" : 'Surrey,CA',
    "appid" : KEY
    }

response = requests.get(url="http://api.openweathermap.org/data/2.5/weather?q=Surrey,CA&appid=28641f35c9c547ab0665ac5e3c8e339b")
print(response.json()["weather"])