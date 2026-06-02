import requests

new_user = {
    "name": "Subhash",
    "username": "subhash08",
    "email": "subhash@example.com"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=new_user
)

print(response.status_code)
print(response.json())

import requests

updated_user = {
    "name": "Subhash",
    "username": "subhash08",
    "email": "subhash@example.com"
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/users/1",
    json=updated_user
)

print(response.status_code)
print(response.json())

import requests

response = requests.delete(
    "https://jsonplaceholder.typicode.com/users/1")

print(response.status_code)