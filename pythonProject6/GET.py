import requests
from info import base_url, date_user

head = {
    'accept': 'application/json'
}

status = 'available'
res_find_by_status = requests.get(f'{base_url}pet/findByStatus?status={status}', headers=head)
if 'application/json' in res_find_by_status.headers['Content-Type']:
    print(res_find_by_status.json())
else:
    print(res_find_by_status.text)

print(res_find_by_status.status_code)
print(type(res_find_by_status.json()))


res_find_by_petID = requests.get(f'{base_url}pet/{date_user["id"]}', headers=head)
if 'application/json' in res_find_by_petID.headers['Content-Type']:
    print(res_find_by_petID.json())
else:
    print(res_find_by_petID.text)

print(res_find_by_petID.status_code)
print(type(res_find_by_petID.json()))


orderID = '444'
res_find_order = requests.get(f'{base_url}store/order/{orderID}', headers=head)
if 'application/json' in res_find_order.headers['Content-Type']:
    print(res_find_order.json())
else:
    print(res_find_order.text)

print(res_find_order.status_code)
print(type(res_find_order.json()))


res_return_by_status = requests.get(f'{base_url}store/inventory', headers=head)
if 'application/json' in res_return_by_status.headers['Content-Type']:
    print(res_return_by_status.json())
else:
    print(res_return_by_status.text)

print(res_return_by_status.status_code)
print(type(res_return_by_status.json()))


res_get_user_byUsername = requests.get(f'{base_url}user/{date_user["username"]}', headers=head)
if 'application/json' in res_get_user_byUsername.headers['Content-Type']:
    print(res_get_user_byUsername.json())
else:
    print(res_get_user_byUsername.text)

print(res_get_user_byUsername.status_code)
print(type(res_get_user_byUsername.json()))


res_logs_user = requests.get(f'{base_url}user/login?username={date_user["username"]}&password={date_user["password"]}', headers=head)
if 'application/json' in res_logs_user.headers['Content-Type']:
    print(res_logs_user.json())
else:
    print(res_logs_user.text)

print(res_logs_user.status_code)
print(type(res_logs_user.json()))


res_logs_out = requests.get(f'{base_url}user/logout', headers=head)
if 'application/json' in res_logs_out.headers['Content-Type']:
    print(res_logs_out.json())
else:
    print(res_logs_out.text)

print(res_logs_out.status_code)
print(type(res_logs_out.json()))
