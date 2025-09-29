# Тест метода создания проекта ( [POST] /api-v2/projects)
import requests
base_url = "https://ru.yougile.com/api-v2"

def get_project_list(params_to_add=None):
    resp = requests.get(base_url + '/projects', params_to_add)
    return resp.json()

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

def test_add_new_project():
    # Получить количество проектов до
    body = get_project_list()
    len_before = len(body) # Находим длину переменной

    # Создать новый проект
    title = "New_pro"
    create_project()

    body = get_project_list()
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["title"] == title