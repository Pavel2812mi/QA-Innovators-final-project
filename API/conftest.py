import pytest
import requests


MAIN_URL = "https://thinking-tester-contact-list.herokuapp.com"

user_data = {
    "email": "testexample@example.com",
    "password": "Tester11"
}


@pytest.fixture(scope="session")
def auth_token():
    """Login as user and get token."""
    response = requests.post(f"{MAIN_URL}/users/login", json=user_data)
    if response.status_code == 200:
        return response.json().get("token")
    else:
        raise Exception(f"Ошибка авторизации: {response.status_code}, {response.text}")


@pytest.fixture(scope="session")
def base_url():
    """Fixture to easify test_api code"""
    return MAIN_URL


@pytest.fixture(scope="function")
def cleanup_contacts(auth_token, base_url):
    """Fixture delete contacts after tests"""
    yield
    url = f"{base_url}/contacts"
    headers = {"Authorization": f"Bearer {auth_token}"}

    response = requests.get(url, headers=headers)
    contacts = response.json()

    for contact in contacts:
        contact_id = contact["_id"]
        delete_url = f"{base_url}/contacts/{contact_id}"
        requests.delete(delete_url, headers=headers)
