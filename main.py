
'''
Smart Taxi API is an intelligent web service for estimating taxi trip costs.

It uses a Machine Learning model to predict the estimated fare based on
trip distance and traffic conditions, with optional LLM and TTS integration
for natural-language explanations and audio output.
'''

__version__ = '1.0.1'

from flask import Flask, jsonify, request
from services.prediction import load_model, predict
from services.llm import load_model_llm, response_chat_qwen
from services.tts import generate_tts

app = Flask(__name__)
MODEL_LLM = load_model_llm()
MODEL = load_model()

@app.get('/')
def main():
    '''Return a welcome message for the Taxi API.'''
    return jsonify(
        status=200,
        data={
            'message': 'Welcome to Taxi API! Your journey starts here.',
            'version': __version__
        }), 200

@app.get('/health')
def health():
    '''Check the health status of the Taxi API.'''
    return jsonify(
        status=200,
        data={
            'message': 'Taxi API is healthy.'
        }), 200

@app.post('/predict')
def prediction():
    '''Generate a prediction from the Taxi API.'''
    distance_get = request.json.get('distance')
    traffic_get = request.json.get('traffic')

    try:
        if not distance_get or not traffic_get:
            return jsonify(status=400, data={'message': '`distance or traffic` is required and must be a non-empty string.'}), 400

        response_pre = predict(model=MODEL, data=[[distance_get, traffic_get]])

        CONTENT_MESSAGE = f'''
        مسافت سفر: {distance_get} کیلومتر
        سطح ترافیک: {traffic_get} از 3
        قیمت پیش‌ بینی‌شده: {round(response_pre, 1)} ریال
    
        در یک پاراگراف کوتاه و فارسی، قیمت سفر را برای کاربر توضیح بده.
        به مسافت و سطح ترافیک اشاره کن.
        عدد جدیدی محاسبه نکن و قیمت را تغییر نده.
        '''

        response_llm = response_chat_qwen(model=MODEL_LLM, prompt=CONTENT_MESSAGE)
        response_tts = generate_tts(text=response_llm)

        return jsonify(status=200, data={'message': 'Predict successfully.', 'response_predict': f'{round(response_pre, 1)}', 'response_llm': f'{response_llm}', 'response_tts': f'{request.host_url}{response_tts}'}), 200
    except Exception as e:
        return jsonify(status=500, data={'message': f'Failed to generate prediction: {str(e)}'}), 500

@app.post('/llm')
def llm():
    '''Generate a response using the LLM.'''
    prompt_get = request.json.get('prompt')

    try:
        if not prompt_get:
            return jsonify(status=400, data={'message': '`prompt` is required and must be a non-empty string.'}), 400

        gen_response = response_chat_qwen(model=MODEL_LLM, prompt=prompt_get)
        return jsonify(status=200, data={'message': 'Response LLM generated successfully.', 'response': f'{gen_response}'}), 200
    except Exception as e:
        return jsonify(status=500, data={'message': f'Failed to generate Response LLM: {str(e)}'}), 500

@app.post('/tts')
def tts():
    '''Convert text to speech.'''
    text_get = request.json.get('text')
    voice_get = request.json.get('voice', 'fa-IR-FaridNeural')

    try:
        if not text_get or not voice_get:
            return jsonify(status=400, data={'message': '`text or voice` is required and must be a non-empty string.'}), 400

        gen_tts_url = generate_tts(text=text_get, voice_type=voice_get)
        return jsonify(status=200, data={'message': 'TTS generated successfully.', 'audio_url': f'{request.host_url}{gen_tts_url}'}), 200
    except Exception as e:
        return jsonify(status=500, data={'message': f'Failed to generate speech: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True)
