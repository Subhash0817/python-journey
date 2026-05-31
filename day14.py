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
