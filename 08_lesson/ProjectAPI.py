import requests
base_url = "https://ru.yougile.com/api-v2"

class ProjectApi:
    def __init__(self, url) -> None:
        self.url = base_url

    # Получить ключ авторизации
    def get_API_key(login="ornela07@mail.ru", password="6IzF%vaZ",
                         companyID="559cf0d9-2619-4890-b9d0-c604b6e65739"):
        creds = {"login": login, "password": password, "companyId": companyID}
        resp = requests.post(base_url + '/auth/keys', json=creds)
        response_key = resp.json()
        if 'key' in response_key:
            return response_key['key']
        else:
            raise ValueError("Токен не найден в ответе API")

    # Получить список проектов
    def get_project_list(self, params_to_add=None):
        resp = requests.get(self.url + '/projects', params=params_to_add)
        return resp.json()

    # Получить проект по id:
    def get_project(self, id):
        resp = requests.get(self.url + '/projects/' + str(id))
        return resp.json()

    # Добавить проект:
    def create_project(self, name):
        project = {"name": name}
        resp = requests.post(self.url + '/projects', json=project)
        return resp.json()

    # Изменить проект:
    def edit_project(self, new_id, new_name):
        key = self.get_API_key()
        url_with_id = f"{self.url}/project/{new_id}"
        project = {"name": new_name}
        resp = requests.put(url_with_id, json=project)



