# Получить проект по ID
import requests
from ProjectAPI import ProjectApi
api = ProjectApi("https://ru.yougile.com")

base_url = "https://ru.yougile.com/api-v2"

def get_API_key(login = "ornela07@mail.ru", password = "6IzF%vaZ", companyID = "559cf0d9-2619-4890-b9d0-c604b6e65739"):
    creds = {"login": login, "password": password, "companyId": companyID}
    resp = requests.post(base_url+'/auth/keys', json=creds)
    response_key = resp.json()
    if 'key' in response_key:
        return response_key['key']
    else:
        raise ValueError("Токен не найден в ответе API")

def create_project():
    headers = {"Authorization": "key", "Content-Type": "application/json"}
    data = {"title": "New_pro1", "users": {"f2d66cdf-21ed-4a73-9046-ec1bb366756b": "admin"}}
    resp = requests.post(base_url + '/projects', json=data)
    return resp.json()

def get_project():
    headers = {"Authorization": "key", "Content-Type": "application/json"}
    resp = requests.get(base_url + '/projects/' + str(id))
    return resp.json()

def test_get_project_id():
    headers = {"Authorization": "key", "Content-Type": "application/json"}
    name = "Newproject1"
    result = api.create_project(name)
    print(result)
    new_id = result['id']

    # Обращаемся к проекту
    new_project = api.get_project(new_id)
    # Проверим название, описание и статус нового проекта:
    assert new_project["name"] == name
    assert new_project["is_active"] is True
