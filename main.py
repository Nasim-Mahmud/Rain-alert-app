import requests
from twilio.rest import Client


api_key = "dd121110304b3377d428a8d4cea4fe5b"
OWN_API = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "ACc65f7f168ddb0c92bbc38453d0e57978"
auth_token = "e24ecdf8af2167e03dc5e49abdaf817e"

parameters = {
    "lat": 23.810331,
    "lon": 90.412521,
    "appid": api_key
}
respond = requests.get(OWN_API, params=parameters)
respond.raise_for_status()

data = respond.json()
print(data["hourly"])
