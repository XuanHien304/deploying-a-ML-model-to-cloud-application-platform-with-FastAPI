"""
Author: HienVX1
Date: 2023/09/12
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
from ml.data import process_data
from ml.model import compute_model_metrics


def slice_census(data, cat_features):
    """ Function for evaluate model on slice of dataset """
    
    train, test = train_test_split(data, test_size=0.20)

    model = joblib.load('model/model.pkl')
    encoder = joblib.load('model/encoder.pkl')
    lb = joblib.load('model/lb.pkl')
    slice_result = {'feature': [], 'category': [], 'precision': [], 'recall': [], 'Fbeta': []}

    for cat in cat_features:
        for cls in test[cat].unique():
            df_temp = test[test[cat] == cls]

            X_test, y_test, _, _ = process_data(
                df_temp, categorical_features=cat_features, label='salary', training=False,
                encoder=encoder, lb=lb
            )

            y_pred = model.predict(X_test)

            precision, recall, fbeta = compute_model_metrics(y_test, y_pred)
            slice_result['feature'].append(cat)
            slice_result['category'].append(cls)
            slice_result['precision'].append(precision)
            slice_result['recall'].append(recall)
            slice_result['Fbeta'].append(fbeta)
    
    df = pd.DataFrame.from_dict(slice_result)
    df.to_csv('slice_output.txt', index=False)

if __name__ == '__main__':
    cat_features = [
        'workclass',
        'education',
        'marital-status',
        'occupation',
        'relationship',
        'race',
        'sex',
        'native-country',
    ]
    data = pd.read_csv('data/census_clean.csv')
    slice_census(data, cat_features)