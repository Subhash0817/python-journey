student = {
    "name" : "subhash",
    "age" : "21",
    "course": "cse"
}
print(student ["name"])
print(student ["age"])
student["age"] = 22


student["skills"] = "Python"

print(student)


student ={}
student["name"] = input("enter student name:")
student["age"] = input("enter student age:")
student["course"] = input("enter student course:")

print(student)



player = {
    "username" : "subhash",
    "level" : "21",
    "score" : "30",
    "weapon": "operator"
}
player ["level"] = 90
print(f"Welcome {player['username']}")
print(f"Player level is {player['level']}")
print(f"Player weapon is {player['weapon']}")


player = {}
player["name"] = input("enter user name:")
player["level"] = input("enter user level:")
player["score"] = input("enter user score:")
player["weapon"] = input("enter user weapon:")

print(player)