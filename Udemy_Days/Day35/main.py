import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall" #the page link where we'll extract the data
api_key = os.environ.get("OWM_API_KEY") # create environment variables (varibales that the other cant see their values sutch as authet)

#the user data of Twilio
account_sid = "YOUR ACCOUNT SID"
auth_token = os.environ.get("AUTH_TOKEN")
api_key = "03b97643b147d7097f5191be8049955d"

#the parameters of our country to put at the link htttp//......
parameters = {
    "lat": 39.983855,
    "lon": -74.732219,
    "appid": api_key,
    "exclude" : "current,minutely,daily" # exclude the paramters that you dont want
}

#connect with the page of the weather data
id_weather = []
reponse = requests.get(OWM_Endpoint, params=parameters)
reponse.raise_for_status()
weather_data = reponse.json()

#get the data only for the 12 first hours of the day
weather_slice = weather_data["hourly"][0:12]
for hourly_weath in weather_slice:
    id_code = hourly_weath['weather'][0]["id"] # the id of the cond of the weather
    if int(id_code) <700:
        will_rain = True

#send sms with twilio
if will_rain:   
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client) 
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_="YOUR TWILIO VIRTUAL NUMBER",
            to="YOUR TWILIO VERIFIED REAL NUMBER"
            )
