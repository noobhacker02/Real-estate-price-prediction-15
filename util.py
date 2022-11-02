import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None


# Pass form data to prediction model
def get_estimated_price(Location, Area, bhk, Lift,Parking):
    try:
        loc_index = __data_columns.index(Location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = Area
    x[1] = bhk
    x[2] = Lift
    x[3] = Parking
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():  
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]  

    global __model
    if __model is None:
        with open('./artifacts/Price_prediction_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("Loading saved artifacts...done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Dombivali',600,2,1,0))