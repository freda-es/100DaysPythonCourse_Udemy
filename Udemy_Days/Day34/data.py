import requests
from datetime import datetime

parameters = {
    "amount": 10,
    "type": "boolean", 
}

reponse = requests.get("https://opentdb.com/api.php", params=parameters)
reponse.raise_for_status()
data = reponse.json()
question_data=data["results"]

