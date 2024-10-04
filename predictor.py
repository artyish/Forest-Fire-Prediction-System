from joblib import load
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


model = load('artifacts/model.joblib')
scaler = load('artifacts/scaler.joblib')

def preprocess_input(input_data):
    expected_columns = ['Temperature','windspeed','fuelmoisturecode','duffmoisturecode','initialspreadindex']
    df = pd.DataFrame(columns=expected_columns,index=[0])

    df['Temperature'] = input_data.get('Temperature', 0)
    df['windspeed'] = input_data.get('Windspeed', 0)
    df['fuelmoisturecode'] = input_data.get('Fuel Moisture Code', 0)
    df['duffmoisturecode'] = input_data.get('Duff Moisture Code', 0)
    df['initialspreadindex'] = input_data.get('Initial Spread Index', 0) 
    
    df = handlescaling(df)
    return df

def handlescaling(df):
    scaler_object = scaler

    columnstoscale = scaler['columnstoscale']
    scaleruse = scaler['scalertest']

    df[columnstoscale] = scaleruse.transform(df[columnstoscale])

    return df 

def predict(input_data):
    print(input_data)
    inputdf = preprocess_input(input_data)

    prediction = model.predict(inputdf)
    print(prediction)

    return prediction