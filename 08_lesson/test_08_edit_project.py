# Тест метода изменение проекта ( [PUT] /api-v2/projects/{id})
import requests
from ProjectAPI import ProjectApi
api = ProjectApi("https://ru.yougile.com")

base_url = "https://ru.yougile.com/api-v2"

def get_token(user = 'ornela07@mail.ru', password = '6IzF%vaZ', companyID = "559cf0d9-2619-4890-b9d0-c604b6e65739"):
    creds = {'username': user, 'password': password, 'companyId': companyID}
    resp = requests.post(base_url+'/auth/keys', json=creds)
    return resp.json()["key"]

def create_project():
    headers = {"Authorization": "key", "Content-Type": "application/json"}
    data = {"title": "New_pro1", "users": {"f2d66cdf-21ed-4a73-9046-ec1bb366756b": "admin"}}
    resp = requests.post(base_url + '/projects', json=data)
    return resp.json()


def test_edit_project(new_id, new_name):
    name =  "New_pro1"
    result = api.create_project(name)
    new_id = result["id"]

    edited = api.edit_project(new_id, new_name)
    assert edited["name"] == new_name



