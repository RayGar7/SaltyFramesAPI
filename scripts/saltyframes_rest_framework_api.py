import requests
import os
import json


AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"

image_path = os.path.join(os.getcwd(), "zoomer.png")

headers = {
    "Content-Type": "application/json",
}

login_data = {
    'username': 'ray',
    'password': env('password'),
}
r = requests.post(AUTH_ENDPOINT, data=json.dumps(login_data), headers=headers)
token = r.json()['token']
print(token)


ENDPOINT = "http://127.0.0.1:8000/api/status/5/"

headers2 = {
    #"Content-Type": "application/json",
    "Authorization": "JWT " + token
}

data2 = {
    'content': 'this new content post'
}

r = requests.put(ENDPOINT, data=json.dumps(data2), headers=headers2)
token = r.json() #['token']

with open(image_path, 'rb') as image:
    file_data = {
        'image': image
    }
    r = requests.put(ENDPOINT, data=data2, headers=headers2, files=file_data)
    print(r.text)

