"""
Author: HienVX1
Date: 2023/09/12
"""
import sys
sys.path.append('.')
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get():
    """ Test the root welcome page """
    r = client.get('/')
    assert r.status_code == 200
    assert r.json() == {'message': 'Hello World'}


def test_post_above():
    """ Test the output for salary is >50k """

    r = client.post('/prediction', json={
        "age": 31,
        "workclass": "Private",
        "fnlgt": 45781,
        "education": "Masters",
        "education-num": 14,
        "marital-status": "Never-married",
        "occupation": "Prof-specialty",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Female",
        "capital-gain": 14084,
        "capital-loss": 0,
        "hours-per-week": 50,
        "native-country": "United-States"
    })

    assert r.status_code == 200
    assert r.json() == {'Predicted Income': ' >50K'}

def test_post_below():
    """ Test the output for salary is <50k """

    r = client.post('/prediction', json={
        "age": 39,
        "workclass": "State-gov",
        "fnlgt": 77516,
        "education": "Bachelors",
        "education-num": 13,
        "marital-status": "Never-married",
        "occupation": "Adm-clerical",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Male",
        "capital-gain": 2174,
        "capital-loss": 0,
        "hours-per-week": 40,
        "native-country": "United-States"
    })

    assert r.status_code == 200
    assert r.json() == {'Predicted Income': ' <=50K'}