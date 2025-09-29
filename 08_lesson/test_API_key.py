# Получить ключ API
import requests
base_url = "https://ru.yougile.com/api-v2"

def test_get_API_key(login = "ornela07@mail.ru", password = "6IzF%vaZ", companyID = "559cf0d9-2619-4890-b9d0-c604b6e65739"):
    creds = {"login": login, "password": password, "companyId": companyID}
    resp = requests.post(base_url+'/auth/keys', json=creds)
    response_key = resp.json()
    if 'key' in response_key:
        return response_key['key']
    else:
        raise ValueError("Токен не найден в ответе API")