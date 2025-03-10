import requests
import pytest
from config import base_url

@pytest.mark.parametrize("id", [1]) # Brackets for Passing id as Int
def test_get_user_by_id(id):
    response = requests.get(f"{base_url}/users/{id}")
    json_response = response.json()
    assert json_response["data"]["id"] == id, f"Expected user id to be {id}, but got {json_response['data']['id']}"

@pytest.mark.parametrize("id", [1]) # Brackets for Passing id as Int
def test_get_single_user_status_code_and_ok(id):
    response = requests.get(f"{base_url}/users/{id}")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.ok, f"Expected response to be OK, but got status code {response.status_code}"

@pytest.mark.parametrize("id", [2]) # Brackets for Passing id as Int
def test_get_single_user_existing_keys(id):
    response = requests.get(f"{base_url}/users/{id}")
    json_response = response.json()
    assert 'data' in json_response.keys(), "'data' key is missing from the response"

