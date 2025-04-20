import pickle
import json
import numpy as np
from sklearn.linear_model._base import LinearRegression
from sklearn.preprocessing import LabelEncoder

__locations = None
__data_columns = None
__model: LinearRegression = None
__label: LabelEncoder = None

def get_estimated_price(location: str, sqft: float, bhk: int, balcony: int, bath: int) -> float:
    return round(__model.predict([[__label.transform([location.lower()])[0], sqft, bath, balcony, bhk]])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    with open("./artifacts/location.json", "r") as f:
        __locations = json.load(f)['locatio_values']

    global __label
    if __label is None:
        with open("./artifacts/location.pickle", "rb") as f:
            __label = pickle.load(f)

    global __model
    if __model is None:
        with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location