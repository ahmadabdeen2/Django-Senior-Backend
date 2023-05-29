import numpy as np
import pickle

def preprocess_features(features):
    # Load the standard scaler
    with open('models/aym_2.pickle', 'rb') as handle:
        Standard_Scaler = pickle.load(handle)
    
    # Convert the list to an array and apply standardization
    features_arr = np.array(features)
    features_arr = Standard_Scaler.transform(features_arr.reshape(1, -1))
    
    return features_arr
