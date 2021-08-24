import requests

def test_get_check_status_code_equals_200():
    response = requests.get("https://reqres.in/api/unknown/2")
    assert response.status_code == 200, "Not error 200"

def test_color():
    response = requests.get("https://reqres.in/api/unknown/2").json()
    items = response["data"].items()
    # print(items)
    assert ('color', '#C74375') in items, "Error"
