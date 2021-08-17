import requests
# import json
def test_get_check_status_code_equals_200():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200, "Not code 200"

def test_get_check_first_name_janet():
    response = requests.get("https://reqres.in/api/users/2").json()
    items = response["data"].items()
    assert ('first_name', 'Janet') in items, "first name is not Janet"
