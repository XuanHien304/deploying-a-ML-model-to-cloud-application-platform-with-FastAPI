"""
Author: HienVX1
Date: 2023/09/12
"""
import sys
sys.path.append('.')
import pandas as pd
import pytest
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from starter.ml.data import process_data

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

def test_data():
    """ Test data csv """

    data = pd.read_csv('data/census_clean.csv')
    assert data.shape[0] > 0


def test_process_data():
    """ Test process data """

    data = pd.read_csv('data/census_clean.csv')
    train, test = train_test_split(data, test_size=0.20)

    X_train, y_train, _, _ = process_data(
        train, categorical_features=cat_features, label="salary", training=True
    )
    assert X_train.shape[0] == y_train.shape[0]


def test_model():
    """ Test Random Forest model """

    model = joblib.load('model/model.pkl')
    assert isinstance(model, RandomForestClassifier)