import requests


def test_delete_user_unauthorized(base_url):
    """TC013: Delete User - 401 Unauthorized "Please
    authenticate."""
    url = f"{base_url}/users/me"
    headers = {}

    response = requests.delete(url, headers=headers)

    assert response.status_code == 401
    assert response.json().get("error") == ("Please "
                                            "authenticate.")


def test_add_contact_success(auth_token, base_url, cleanup_contacts):
    """TC014: Add Contact - 201 Created"""
    url = f"{base_url}/contacts"
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    body = {
        "firstName": "John",
        "lastName": "Doe",
        "birthdate": "1970-01-01",
        "email": "jdoe@fake.com",
        "phone": "8005555555",
        "street1": "1 Main St.",
        "street2": "Apartment A",
        "city": "Anytown",
        "stateProvince": "KS",
        "postalCode": "12345",
        "country": "USA"
    }

    response = requests.post(url, json=body, headers=headers)

    assert response.status_code == 201
    data = response.json()
    assert data["firstName"] == "John"
    assert data["lastName"] == "Doe"
    assert data["owner"] is not None


def test_add_contact_unauthorized(base_url):
    """TC015: Add Contact - 401 Unauthorized "Please
    authenticate."""
    url = f"{base_url}/contacts"
    headers = {}
    body = {
        "firstName": "John",
        "lastName": "Doe",
        "birthdate": "1970-01-01",
        "email": "jdoe@fake.com",
        "phone": "8005555555",
        "street1": "1 Main St.",
        "street2": "Apartment A",
        "city": "Anytown",
        "stateProvince": "KS",
        "postalCode": "12345",
        "country": "USA"
    }

    response = requests.post(url, json=body, headers=headers)

    assert response.status_code == 401
    assert response.json().get("error") == ("Please "
                                            "authenticate.")


def test_add_contact_bad_request(auth_token, base_url, cleanup_contacts):
    """TC016: Add Contact - 400 Bad Request"""
    url = f"{base_url}/contacts"
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    body = {}

    response = requests.post(url, json=body, headers=headers)

    assert response.status_code == 400

    response_json = response.json()

    assert "errors" in response_json
    assert "_message" in response_json
    assert "message" in response_json

    assert "firstName" in response_json["errors"]
    assert "lastName" in response_json["errors"]

    assert (response_json["errors"]["firstName"]["message"] ==
            "Path `firstName` is required.")
    assert (response_json["errors"]["lastName"]["message"] ==
            "Path `lastName` is required.")


def test_get_contact_list_success(auth_token, base_url, cleanup_contacts):
    """TC017: Get Contact List - 200 OK"""
    url = f"{base_url}/contacts"
    headers = {
        "Authorization": f"Bearer {auth_token}",
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        contact = data[0]
        assert "firstName" in contact
        assert "lastName" in contact


def test_get_contact_list_unauthorized(base_url):
    """TC018: Get Contact List - 401 Unauthorized
    "Please authenticate."""
    url = f"{base_url}/contacts"
    headers = {}

    response = requests.get(url, headers=headers)

    assert response.status_code == 401
    assert response.json().get("error") == ("Please "
                                            "authenticate.")
