import requests
import pytest


@pytest.mark.skip(reason="Public API may be rate limited")
def test_users_api():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200
