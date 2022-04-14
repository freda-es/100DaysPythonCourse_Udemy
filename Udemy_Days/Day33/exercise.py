# #call the library that requests API
# import requests
# #create a variable whitch gives us the data from the webpage ith the requests module
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# #method of raising an exception (when the page does not exist....)
# response.raise_for_status()
# # take this data and create a json file
# data = response.json()
# # now data is same as a dictionary
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)



# -----Parameters for API-------
import requests
from datetime import datetime
MY_LAT = 41.327545
MY_LONG = 19.818699
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted":0,
    
}
reponse = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
reponse.raise_for_status()
data = reponse.json()
sunrise = data["results"]['sunrise']
sunset = data["results"]['sunset']
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)


