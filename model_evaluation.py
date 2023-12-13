import pickle
import joblib
import numpy as np

# Load the pickled model
with open('model.pkl', 'rb') as model_file:
    loaded_model_pickle = pickle.load(model_file)

# Load the joblib model
loaded_model_joblib = joblib.load('model.joblib')

# New data for prediction
new_data = np.array([[5.1, 3.5, 1.4, 0.2]])

# Predict with the pickled model
prediction_pickle = loaded_model_pickle.predict(new_data)
print(f"Prediction using Pickle: {prediction_pickle[0]}")

# Predict with the joblib model
prediction_joblib = loaded_model_joblib.predict(new_data)
print(f"Prediction using Joblib: {prediction_joblib[0]}")
