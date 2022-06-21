import requests

api_key = "dd121110304b3377d428a8d4cea4fe5b"


parameters = {
    "lat": 23.810331,
    "lon": 90.412521,
    "appid": api_key
}
respond = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
respond.raise_for_status()

data = respond.json()
print(data["hourly"])
