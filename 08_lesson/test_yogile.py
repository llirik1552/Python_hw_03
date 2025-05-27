import pytest
import requests

BASE_URL = "https://ru.yougile.com/api-v2/projects"
AUTH_URL = "https://ru.yougile.com/api-v2/auth/keys"
LOGIN_DATA = {
    "login": "ВВЕДИТЕ АДРЕС ЭЛЕКТРОННОЙ ПОЧТЫ",
    "password": "ВВЕДИТЕ ПАРОЛЬ",
    "companyId": "ВВЕДИТЕ ID КОМПАНИИ"
}

@pytest.fixture(scope="module")
def token():
    """Фикстура для получения токена"""
    response = requests.post(AUTH_URL, json=LOGIN_DATA)
    if response.status_code == 201:
        return response.json()["key"]
    else:
        pytest.fail("Failed to get token: {}".format(response.json()))

@pytest.fixture(scope="module")
def headers(token):
    """Фикстура для заголовков с токеном."""
    return {'Authorization': f'Bearer {token}'}

class TestProjects:

    def test_create_project_success(self, headers):
        data = {"title": "Новая компания"}
        response = requests.post(BASE_URL, json=data, headers=headers)
        assert response.status_code == 201
        assert "id" in response.json()

    def test_create_project_failure(self, headers):
        response = requests.post(BASE_URL, json={}, headers=headers)
        assert response.status_code == 400

    def test_get_project_success(self, headers):
        data = {"title": "Project to Get"}
        create_response = requests.post(BASE_URL, json=data , headers=headers)
        project_id = create_response.json().get('id')

        response = requests.get(f"{BASE_URL}/{project_id}", headers=headers)
        assert response.status_code == 200
        assert response.json()['title'] == "Project to Get"

    def test_get_nonexistent_project(self, headers):
        non_existent_id = 9999999
        response = requests.get(f"{BASE_URL}/{non_existent_id}", headers=headers)
        assert response.status_code == 404

    def test_update_project_success(self, headers):
        data = {"title": "Project to Update"}
        create_response = requests.post(BASE_URL, json=data, headers=headers)
        project_id = create_response.json().get('id')

        update_data = {"title": "Updated Project Name"}
        response = requests.put(f"{BASE_URL}/{project_id}", json=update_data, headers=headers)
        assert response.status_code == 200

        response = requests.get(f"{BASE_URL}/{project_id}", headers=headers)
        assert response.status_code == 200
        assert response.json()['title'] == "Updated Project Name"

    def test_update_nonexistent_project(self, headers):
        non_existent_id = 9999999
        update_data = {"title": "Updated Name"}
        response = requests.put(f"{BASE_URL}/{non_existent_id}", json=update_data, headers=headers)
        assert response.status_code == 404