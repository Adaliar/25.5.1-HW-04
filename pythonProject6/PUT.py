import requests
import json
from info import base_url, date_user_2, header


data_update_pet = {
    "id": 222,
    "category": {
        "id": 222,
        "name": "string"
    },
    "name": "Roxy",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 222,
            "name": "string"
        }
    ],
    "status": "available"
}
res_update_pet = requests.put(f'{base_url}pet', headers=header, data=json.dumps(data_update_pet))
if 'application/json' in res_update_pet.headers['Content-Type']:
    print(res_update_pet.json())
else:
    print(res_update_pet.text)

print(res_update_pet.status_code)
print(type(res_update_pet.json()))

data_pp = date_user_2
username_to_upd = 'Stay'
res_update_user = requests.put(f'{base_url}user/{username_to_upd}', headers=header, data=json.dumps(data_pp))
if 'application/json' in res_update_user.headers['Content-Type']:
    print(res_update_user.json())
else:
    print(res_update_user.text)

print(res_update_user.status_code)
print(type(res_update_user.json()))


