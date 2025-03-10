import requests
import pytest
from cerberus import Validator

@pytest.mark.parametrize("email, password", [("eve.holt@reqres.in", "pistol")])
def test_register_user_schema_structure(email, password):
    schema = {
        "id": {"type": "number"},
        "token": {"type": "string"}
    }
    validator = Validator(schema, require_all = True)
    register_user_data = {
        "email": email,
        "password": password
    }
    response = requests.post(
        url = "https://reqres.in/api/register",
        json = register_user_data
    )
    if response.status_code == 200:
        is_valid = validator.validate(response.json())
        assert is_valid

@pytest.mark.parametrize("id", [2]) # Brackets for Passing id as Int
def test_get_single_user_schema_structure(id):
    schema = {
        "data": {
            "type": "dict",
             "schema": {
                 "id": {"type": "number"},
                 "email": {"type": "string"},
                 "first_name": {"type": "string"},
                 "last_name": {"type": "string"},
                 "avatar": {"type": "string"}
             }
         },
        "support": {
            "type": "dict",
            "schema": {
                "url": {"type": "string"},
                "text": {"type": "string"}
            }
        }
    }
    validator = Validator(schema, require_all = True)

    response = requests.get(f"http://reqres.in/api/users/{id}")
    if response.status_code == 200:
        is_valid = validator.validate(response.json())
        assert is_valid

