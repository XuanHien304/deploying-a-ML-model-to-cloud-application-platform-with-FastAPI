"""
Author: HienVX1
Date: 2023/09/12
"""

import pandas as pd
import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from starter.ml.data import process_data
from starter.ml.model import inference

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

class TaggedItem(BaseModel):
    age: int = Field(examples=[39])
    workclass: str = Field(examples=['State-gov'])
    fnlgt: int = Field(examples=[77516])
    education: str = Field(examples=['Bachelors'])
    education_num: int = Field(alias='education-num', examples=[13])
    marital_status: str = Field(alias='marital-status', examples=['Never-married'])
    occupation: str = Field(examples=['Adm-clerical'])
    relationship: str = Field(examples=['Not-in-family'])
    race: str = Field(examples=['White'])
    sex: str = Field(examples=['Male'])
    capital_gain: int = Field(alias='capital-gain', examples=[2174])
    capital_loss: int = Field(alias='capital-loss', examples=[0])
    hours_per_week: int = Field(alias='hours-per-week', examples=[40])
    native_country: str = Field(alias='native-country', examples=['United-States'])


# create app
app = FastAPI()

@app.on_event("startup")
async def startup_event(): 
    global model, encoder, lb
    model = joblib.load('model/model.pkl')
    encoder = joblib.load('model/encoder.pkl')
    lb = joblib.load('model/lb.pkl')

@app.get('/')
async def hello():
    return {'message': 'Hello World'}


@app.post('/prediction')
async def predict(input_data: TaggedItem):
    data = pd.DataFrame({k: v for k,v in input_data.dict(by_alias=True).items()}, index=[0])
    X, _, _, _ = process_data(
                    data, categorical_features=cat_features, label=None, training=False,
                    encoder=encoder, lb=lb
                )
    y_pred = inference(model, X)

    return {'Predicted Income': lb.inverse_transform(y_pred)[0]}

if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=5000, reload=True)