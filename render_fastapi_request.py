"""
Author: HienVX1
Date: 2023/09/12
"""

import requests

url = ''

input_data = {
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
}

req = requests.post(url, json=input_data)
assert req.status_code == 200

print('Status code:', req.status_code)
print('')