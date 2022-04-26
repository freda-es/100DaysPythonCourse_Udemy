import requests
from datetime import datetime

#global variables
USERNAME = "YOUR USERNAME"
TOKEN = "YOUR TOKEN"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"


# # create the user:
user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


#create the graph with the paramters that you want
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name":"Walking steps",
    "unit":"steps",
    "type":"int",
    "color":"shibafu"
}
#tool to login with your token
headers = {
    "X-USER-TOKEN":TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)



#post to the graph
postpx_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

postpx_params = {
    "date":today.strftime("%Y%m%d"),#convert the datetime as a string YYYYMMD
    "quantity":"1566",
        
}
# response = requests.post(url=postpx_endpoint, json=postpx_params, headers=headers)
# print(response.text)



#update the data
#set the parameter data that you want to update
yesterday = datetime(year=2022, month=4, day=21).strftime("%Y%m%d")
updatepx_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"
updatepx_params = {
    "quantity":"1400",        
}
# response = requests.put(url=updatepx_endpoint, json=updatepx_params, headers=headers)
# print(response.text)


#delete a pixel yesterday data
response = requests.delete(url=updatepx_endpoint, headers=headers)
print(response.text)