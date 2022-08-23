import requests
from twilio.rest import Client

account_sid = "AC8ce8f8153438ab4fc94909710879a6a1"
auth_token = "0edd6c1605d6cc8923039a4db09167b6"

parameters = {
    "lat": 24.446430,
    "lon": -104.123657,
    "exclude": "current,minutely,daily",
    "appid": "0c08defaff8ea71a860b5f0bb51795cb"
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
        from_='+15306758720',
        to='+526141695881'
        )


