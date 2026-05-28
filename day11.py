"""list comprehension"""
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [number for number in numbers if number %2 == 0]
print(even_numbers)
odd_numbers = [number for number in numbers if number %2 != 0]
print(odd_numbers)

names = ["subhash", "v", "sage"]
upper_names = [name.upper() for name in names]
print(upper_names)


names = ["subhash", "v", "sage", "sova", "jett"]

filtered_names = [name for name in names if name.startswith("s")]

print(filtered_names)


weapons = [
    {"name": "vandal", "damage": 160},
    {"name": "ghost", "damage": 80},
    {"name": "operator", "damage": 250}
]
filtered_weapons =[
    weapon for weapon in weapons 
    if weapon ["damage"] > 100
]
print(filtered_weapons)

players = [
    {"name": "subhash", "score": 90},
    {"name": "v", "score": 40},
    {"name": "sage", "score": 75}
]


filtered_players = [
    player for player in players
    if player ["score"] >= 70
]
file = open("leaderboard.txt", "w")
for player in filtered_players:
    file.write(f"{player['name']} - {player['score']}\n")
file.close()
print(filtered_players)
