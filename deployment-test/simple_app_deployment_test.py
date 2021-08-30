import requests

expected_response_text = 'Depop Interview Demo!'

def test_simple_app_running(url):
    response = requests.get(url)
    assert response.status_code == 200
    assert response.text == expected_response_text

