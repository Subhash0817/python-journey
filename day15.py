import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    print(response.status_code)

except Exception as e:
    print("Something went wrong")
    print(e)

import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/SDGD"
    )

    print(response.status_code)

except Exception as e:
    print("Something went wrong")
    print(e)

import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/abcd"
)

if response.status_code == 200:
    print("Success")
else:
    print("Error:", response.status_code)






"""Mini API Checker Project"""

import requests
url = input("enter URL: ")

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("website is working")
    else:
        print("website returned", response.status_code)
except   Exception  as e:
    print("connection failed ")
    print(e)