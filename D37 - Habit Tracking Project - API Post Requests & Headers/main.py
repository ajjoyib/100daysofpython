import requests
from datetime import datetime

## CREATE A USER ACCOUNT
USERNAME = "ajjoyib"
TOKEN = "M5x9U9P32Gyq5A8U"
GRAPH_ID = "graph01"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
 

# # Create a user account. (Can be commented out after an initial use)
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)


## CREATE A GRAPH
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# # Create a graph. (Can be commented out after the initial use)
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

## ADD A PIXEL TO THE GRAPH
today = datetime.today()

PIXEL_ADDING_ENDPONIT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

# # Add a pixel to the graph. 
# response = requests.post(url=PIXEL_ADDING_ENDPONIT, json=pixel_config, headers=headers)
# print(response.text)

## UPDATE THE PIXEL OF THE GRAPH
# PIXEL_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
PIXEL_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{20230919}"

updatedelete_config = {
    "quantity": "30",
}

# # Update the pixel on a specified day. (Can be commented out after the initial use)
# response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=update_config, headers=headers)
# print(response.text)


## DELETE THE PIXEL OF THE GRAPH
# PIXEL_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
PIXEL_DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{20230919}"

response = requests.delete(url=PIXEL_DELETE_ENDPOINT, headers=headers)
print(response.text)