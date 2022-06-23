import requests
from twilio.rest import Client

api_key = "[API KEY FROM OPENWEATHER]"
OWN_API = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "[ACCOUNT SID FROM TWILIO]"
auth_token = "[AUTH TOKEN FROM TWILIO]"

parameters = {
    "lat": 93.810331,  # LATITUDE OF YOUR CURRENT POSITION
    "lon": 20.412521,  # LATITUDE OF YOUR CURRENT POSITION
    "appid": api_key,
    "exclude": "current,minutely,daily"  # EXCLUDING THE DATA WE DON'T NEED
}
response = requests.get(OWN_API, params=parameters)
response.raise_for_status()

data = response.json()

# weather_data = data["hourly"][0]["weather"][0]["id"]
weather_slice = data["hourly"][:12]  # RETRIEVING THE DATA OF FIRST TWELVE HOURS
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
        from_="TWILIO TRIAL PHONE NUMBER",  # Got the number from Twilio.
        to="THE PHONE NUMBER YOU USED TO SIGNUP TWILIO"
    )
    print(message.status)
