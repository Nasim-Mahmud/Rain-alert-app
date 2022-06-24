import requests
from twilio.rest import Client

api_key = "46ed3d081d09cf1a51799cc559841c55"
OWN_API = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "ACc65f7f168ddb0c92bbc38453d0e57978"
auth_token = "68fd64c1a02cd127eb265aa42cf3dcbb"

parameters = {
    "lat": 23.810331,  # LATITUDE OF YOUR CURRENT POSITION
    "lon": 90.412521,  # LATITUDE OF YOUR CURRENT POSITION
    "appid": api_key,
    "exclude": "current,minutely,daily"  # EXCLUDING THE DATA WE DON'T NEED
}
response = requests.get(OWN_API, params=parameters)
response.raise_for_status()

data = response.json()

# weather_data = data["hourly"][0]["weather"][0]["id"]
weather_slice = data["hourly"][:24]  # RETRIEVING THE DATA OF FIRST TWELVE HOURS
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
        from_="+19783893832",  # Got the number from Twilio.
        to="+8801884331851"
    )
    print(message.status)
