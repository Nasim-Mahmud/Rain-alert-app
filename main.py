import requests
from twilio.rest import Client


api_key = "dd121110304b3377d428a8d4cea4fe5b"
OWN_API = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "ACc65f7f168ddb0c92bbc38453d0e57978"
auth_token = "e24ecdf8af2167e03dc5e49abdaf817e"

parameters = {
    "lat": 23.810331,
    "lon": 90.412521,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWN_API, params=parameters)
response.raise_for_status()

data = response.json()

# weather_data = data["hourly"][0]["weather"][0]["id"]
weather_slice = data["hourly"][:12]
# print(weather_slice)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It may rain today! Bring an umbrella.",
        from_='+15017122661',
        to='+15558675310'
    )
