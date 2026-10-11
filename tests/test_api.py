
'''Contains tests for the API endpoints.'''

from requests import get, post

URL_HOST = 'http://127.0.0.1:5000/'

def test_health():
    response = get(url=URL_HOST + '/health').status_code
    assert response == 200

def test_prediction():
    response = post(url=URL_HOST + '/predict', json={'distance': 6.5, 'traffic': 2}).status_code
    assert response == 200

def test_invalid_distance():
    response = post(url=URL_HOST + '/predict', json={'distance': '2', 'traffic': 2}).status_code
    assert response == 200

def test_invalid_traffic():
    response = post(url=URL_HOST + '/predict', json={'distance': 2, 'traffic': '2'}).status_code
    assert response == 200

def test_empty_distance():
    response = post(url=URL_HOST + '/predict', json={'distance': '', 'traffic': 1}).status_code
    assert response == 200

def test_empty_traffic():
    response = post(url=URL_HOST + '/predict', json={'distance': 2.5, 'traffic': ''}).status_code
    assert response == 200
