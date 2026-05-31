player = {
    "name": "Subhash",
    "level": 21,
    "health": 100
}

print(player)

import json
player = {
    "name": "Subhash",
    "level": 21,
    "health": 100
}

player_json = json.dumps(player)

print(player_json)
 
import json

player_json = '{"name":"Subhash","level":21,"health":100}'

player_dict = json.loads(player_json)

print(player_dict)
print(type(player_dict))

import json

player = {
    "name": "Subhash",
    "level": 21,
    "health": 100
}

with open("player.json", "w") as file:
    json.dump(player, file)

print("Saved successfully")

import json

with open("player.json", "r") as file:
    player_data = json.load(file)

print(player_data)
print(type(player_data))


import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

print(response.status_code)

user = response.json()

print(user["name"])
print(user["username"])
print(user["phone"])
print(user["email"])


import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)
users = response.json()

name = input("Enter username: ")

for user in users:
    if user["username"].lower() == name.lower():
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("Phone:", user["phone"])
        print("website:", user["website"])
        print("company:", user["company"])
        print("city:", user["city"])
        break
else:
    print("User not found")
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