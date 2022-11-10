if 'application/json' in res.headers['Content-Type']:
    print(res.json())
else:
    print(res.text)

print(res.status_code)
print(type(res.json()))

