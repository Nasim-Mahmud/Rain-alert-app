import requests
from twilio.rest import Client

# API from OpenWeather
api_key = "[OPENWEATHER_API_]"
OWN_API = "https://api.openweathermap.org/data/2.5/onecall"

# API from TWILIO
account_sid = "[TWILIO_ACC_SID_]"
auth_token = "[AUTH_TOKEN_]"

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
        from_="[TWILIO_PROVIDED_NUMBER]",  # Got the number from Twilio.
        to="[PHONE_NUMBER_YOU_REGISTERED_WHILE_CREATING_TWILIO_ACCOUNT]"
    )
    print(message.status)
