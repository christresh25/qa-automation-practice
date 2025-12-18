import requests
import pytest

BASE_URL = "https://reqres.in"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

def test_user_api():
    response = requests.get(
        f"{BASE_URL}/api/users?page=2",
        headers=HEADERS
    )

    if response.status_code == 403:
        pytest.skip("Reqres API blocked / rate limited")

    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) > 0


def test_create_user():
    payload = {
        "name": "reshma",
        "job": "QA Engineer"
    }

    response = requests.post(
        f"{BASE_URL}/api/users",
        json=payload,
        headers=HEADERS
    )

    if response.status_code == 403:
        pytest.skip("Reqres API blocked / rate limited")

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "reshma"
