import requests
from datetime import datetime

#determine the parameters whitch gives us the model of the data that we'll get from API
parameters = {
    "amount": 10,
    "type": "boolean", 
}

#Api procedure and the database of the data/questions are saved as a dictionary
reponse = requests.get("https://opentdb.com/api.php", params=parameters)
reponse.raise_for_status()
data = reponse.json()
question_data=data["results"]

