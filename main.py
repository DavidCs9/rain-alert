import requests
from twilio.rest import Client

account_sid = "yourkeys"
auth_token = "yourkeys"
parameters = {
    "lat": "yourlat",
    "lon": "yourlon",
    "exclude": "current,minutely,daily",
    "appid": "yourkeys"
}


will_rain = False

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]
for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Va a llover. Ponte una chamarra!!. ☂️",
        from_='+theirnumber',
        to='+yourname'
        )


