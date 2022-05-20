import json

import requests


def log_in(mail, password, tel_id):
    url = "https://best-routes.herokuapp.com/user/login"
    mail = "resh@grail.com"
    password = "resh1"

    payload = json.dumps({
        "email": mail,
        "password": password
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def register(mail, password, tel_id):
    mail = "resh@grail.com"
    password = "resh1"
    url = "https://best-routes.herokuapp.com/user/register"

    payload = "{\n    \"email\":" + "\"" + mail + "\"" + ",\n    \"password\": " + "\"" + password + "\"" + "\n}"
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    print(payload)
