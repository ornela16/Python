import requests

base_url = "https://ru.yougile.com/api-v2"
API_key = ""
headers = {"Authorization": "Bearer " + API_key, "Content-Type": "application/json"}

def test_create_project():
    data = {"title": "New_pro1", "users": {"f2d66cdf-21ed-4a73-9046-ec1bb366756b": "admin"}}
    resp = requests.post(base_url + '/projects', json=data, headers=headers)
    assert resp.status_code == 201
    assert resp.json()["id"] is not None

def test_get_project():
    data = {"title": "Newproject", "users": {"f2d66cdf-21ed-4a73-9046-ec1bb366756b": "admin"}}
    resp = requests.post(base_url + '/projects', json=data, headers=headers)
    id = resp.json()["id"]
    resp2 = requests.get(base_url + '/projects/' + str(id), headers=headers)
    assert resp2.status_code == 200
    # Проверим название нового проекта:
    assert resp2.json()["title"] == "Newproject"


def test_edit_project():
    data = {"title": "First_project", "users": {"f2d66cdf-21ed-4a73-9046-ec1bb366756b": "admin"}}
    resp = requests.post(base_url + '/projects', json=data, headers=headers)
    id = resp.json()["id"]
    data = {"title": "Second_project"}
    edited = requests.put(base_url + '/projects/' + str(id), json=data, headers=headers)
    assert resp.json()["id"] is not None
    assert edited.status_code == 200
    resp2 = requests.get(base_url + '/projects/' + str(id), headers=headers)
    assert resp2.status_code == 200
    # Проверим название нового проекта:
    assert resp2.json()["title"] == "Second_project"