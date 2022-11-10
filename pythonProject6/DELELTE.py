import requests
from info import base_url, date_user, date_user_2


res_delete_pet = requests.delete(f'{base_url}pet/{date_user["id"]}')
print(res_delete_pet.json())
print(res_delete_pet.text)
print(res_delete_pet.status_code)
print(type(res_delete_pet.json()))

orderID = 444
res_delete_order = requests.delete(f'{base_url}store/order/{orderID}')
print(res_delete_order.json())
print(res_delete_order.text)
print(res_delete_order.status_code)
print(type(res_delete_order.json()))


res_delete_user = requests.delete(f'{base_url}user/{date_user_2["username"]}')
print(res_delete_user.json())
print(res_delete_user.text)
print(res_delete_user.status_code)
print(type(res_delete_user.json()))
