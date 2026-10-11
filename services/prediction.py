
'''Provides services for generating predictions.'''

from joblib import load
from utils.logger import generate_log

MODEL_PATH = 'models\\trained\\model-trained-v1.0.1.pkl'

def load_model():
    try:
        model = load(MODEL_PATH)
        
        generate_log(text='Model loaded successfully.', log_type='SUCCESS')
        return model
    except FileNotFoundError:
        generate_log(text='Model is not loaded.', log_type='ERROR')
        return None
    except Exception as e:
        generate_log(text=str(e), log_type='ERROR')
        return None

def predict(model, data):
    generate_log(text='Predict successfully.', log_type='SUCCESS')
    return model.predict(data)[0]
