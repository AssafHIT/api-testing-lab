import requests
import pytest
from config import base_url

@pytest.mark.parametrize("id", [2]) # Brackets for Passing id as Int
def test_delete_user_by_id(id):
    response = requests.delete(f"{base_url}/users/{id}")
    assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"