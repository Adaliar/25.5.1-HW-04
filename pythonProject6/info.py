from requests_toolbelt.multipart.encoder import MultipartEncoder
import os

base_url = 'https://petstore.swagger.io/v2/'
header = {
    'accept': 'application/json', 'Content-Type': 'application/json'
}

pet_info = {
    "id": 222,
    "category": {
        "id": 222,
        "name": "Roxy"
    },
    "name": "Roxy",
    "photoUrls": [
        "https://yandex.ru/images/search?pos=6&img_url=http%3A%2F%2Fmobimg.b-cdn.net%2Fv3%2Ffetch%2F92%2F92fc3bc2ce63665b89c57294fd21d18d.jpeg&text=картинка%20кошки&lr=43&rpt=simage&source=serp"
    ],
    "tags": [
        {
            "id": 222,
            "name": "Roxy"
        }
    ],
    "status": "available"
}


class Photo:
    file_name = "cat.jpg"
    pet_photo = os.path.join(os.path.dirname(__file__), f"images/{file_name}")
    image_data = MultipartEncoder(fields={"file": (file_name, open(pet_photo, 'rb'), 'image/jpeg')})


date_user = {
    "id": 222,
    "username": "Stay",
    "firstName": "Bill",
    "lastName": "Bowl",
    "email": "email",
    "password": "password",
    "phone": "123456789",
    "userStatus": 1
}

date_user_2 = {
    "id": 222,
    "username": "Bias",
    "firstName": "Bill",
    "lastName": "Bowl",
    "email": "email",
    "password": "password",
    "phone": "123456789",
    "userStatus": 1
}
