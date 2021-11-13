import requests
from datetime import datetime

parameters = {
    "lng": -122.843671,
    "lat": 49.202381,
    'formatted': 0
}
api_url = "https://api.sunrise-sunset.org/json"


response = requests.get(url=api_url, params=parameters)
results = response.json()['results']

print(results)

time_now = datetime.now()