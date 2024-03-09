import requests
from datetime import datetime

USERNAME="kstc707"
TOKEN="asdfghjkl"
ID="graph1"

pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOFService": "yes",
    "notMinor": "yes"
}

#
# response = requests.post(url=pixela_endpoint,json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": ID,
    "name": "Udemy Graph",
    "unit": "min",
    "type": "float",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
today=datetime.now()
DATE= today.strftime("%Y%m%d")
post_config={
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you study today? ")
}
response = requests.post(url=post_endpoint,json=post_config,headers=headers)
print(response.text)

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{DATE}"
put_config={
    "quantity": "110"
}
# response = requests.put(url=put_endpoint,json=put_config,headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{DATE}"
# response = requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)