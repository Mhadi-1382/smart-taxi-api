
'''Provides text-to-speech conversion services.'''

from edge_tts import Communicate
from secrets import token_urlsafe
from os import makedirs
from utils.logger import generate_log

makedirs('static/tts', exist_ok=True)

VOICE_TYPE = {
    'fa-IR-FaridNeural': 'fa-IR-FaridNeural',
    'fa-IR-DilaraNeural': 'fa-IR-DilaraNeural',
    'en-US-RogerNeural': 'en-US-RogerNeural'
}

def generate_tts(text: str, voice_type: str = VOICE_TYPE['fa-IR-FaridNeural']):
    try:
        pattern_file = f'static/tts/tts_{token_urlsafe(20)}.mp3'
        Communicate(text=text, voice=voice_type).save_sync(audio_fname=pattern_file)
        generate_log(text='TTS generated successfully.', log_type='SUCCESS')
        return pattern_file
    except Exception as e:
        generate_log(text=e, log_type='ERROR')
        return None
