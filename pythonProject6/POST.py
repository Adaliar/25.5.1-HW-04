import requests
import json

from info import base_url, pet_info, Photo, header, date_user


head_pet_img = {
    'accept': 'application/json', "Content-Type": Photo.image_data.content_type
}
res_upload_img = requests.post(f"{base_url}pet/{date_user['id']}/uploadImage", headers=head_pet_img,
                               data=Photo.image_data)
if 'application/json' in res_upload_img.headers['Content-Type']:
    print(res_upload_img.json())
else:
    print(res_upload_img.text)

print(res_upload_img.status_code)
print(type(res_upload_img.json()))


res_add_pet = requests.post(f"{base_url}pet", headers=header, data=json.dumps(pet_info))
if 'application/json' in res_add_pet.headers['Content-Type']:
    print(res_add_pet.json())
else:
    print(res_add_pet.text)

print(res_add_pet.status_code)
print(type(res_add_pet.json()))


date_update = {
    'name': 'RM', 'status': 'available'
}
head_update = {
    'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'
}
res_update_form_data = requests.post(f"{base_url}pet/{date_user['id']}", headers=head_update, data=date_update)
if 'application/json' in res_update_form_data.headers['Content-Type']:
    print(res_update_form_data.json())
else:
    print(res_update_form_data.text)

print(res_update_form_data.status_code)
print(type(res_update_form_data.json()))


data_pet_order = {
    'id': 444,
    'petId': 222,
    'quantity': 0,
    'shipDate': '2022-11-09T08:28:13.624Z',
    'status': 'placed',
    'complete': True
}
res_pet_order = requests.post(f'{base_url}store/order', headers=header, data=json.dumps(data_pet_order))
if 'application/json' in res_pet_order.headers['Content-Type']:
    print(res_pet_order.json())
else:
    print(res_pet_order.text)

print(res_pet_order.status_code)
print(type(res_pet_order.json()))


data_user_list = [date_user]
res_with_array = requests.post(f'{base_url}user/createWithArray', headers=header, data=json.dumps(data_user_list))
if 'application/json' in res_with_array.headers['Content-Type']:
    print(res_with_array.json())
else:
    print(res_with_array.text)

print(res_with_array.status_code)
print(type(res_with_array.json()))


res_with_list = requests.post(f'{base_url}user/createWithList', headers=header, data=json.dumps(data_user_list))
if 'application/json' in res_with_list.headers['Content-Type']:
    print(res_with_list.json())
else:
    print(res_with_list.text)

print(res_with_list.status_code)
print(type(res_with_list.json()))

res_create_user = requests.post(f'{base_url}user', headers=header, data=json.dumps(date_user))
if 'application/json' in res_create_user.headers['Content-Type']:
    print(res_create_user.json())
else:
    print(res_create_user.text)

print(res_create_user.status_code)
print(type(res_create_user.json()))
