## Model Deployment using Pickle and Joblib

### Overview

This repository demonstrates the process of saving and loading machine learning models using both `pickle` and `joblib` in Python. The example uses a logistic regression model trained on the Iris dataset.

### Contents

- **`model_training.py`**: Python script for training a logistic regression model on the Iris dataset and saving it using both `pickle` and `joblib`.

- **`model_evaluation.py`**: Python script for loading the saved models and making predictions on new data.

- **`requirements.txt`**: File containing the required Python libraries and their versions.

### Instructions

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train and Save the Model:**
   ```bash
   python model_training.py
   ```

4. **Evaluate the Model:**
   ```bash
   python model_evaluation.py
   ```

### Project Structure

- **`model.pkl`**: Pickle file containing the trained logistic regression model.

- **`model.joblib`**: Joblib file containing the trained logistic regression model.

### Notes

- The `model_training.ipynb` script trains a logistic regression model on the Iris dataset, evaluates its accuracy, and saves it using both `pickle` and `joblib`.

- The `model_evaluation.py` script loads the saved models and makes predictions on new data (`new_data.csv`).

- The `requirements.txt` file specifies the required Python libraries and their versions.

### References

- [scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Pickle Documentation](https://docs.python.org/3/library/pickle.html)
- [Joblib Documentation](https://joblib.readthedocs.io/en/latest/)

Feel free to customize this structure and documentation to fit your specific needs.