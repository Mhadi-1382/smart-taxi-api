
'''Provides services for interacting with the language model.'''

from llama_cpp import Llama
from utils.logger import generate_log

MODEL_NAME = '.\\models\\trained\\qwen2.5-0.5b-instruct-q4_k_m.gguf'

def load_model_llm():
    try:
        llm = Llama(
            model_path=MODEL_NAME,
            n_ctx=2048,
            verbose=False,
            n_threads=6
        )
    
        generate_log(text='Model LLM loaded successfully.', log_type='SUCCESS')
        return llm
    except Exception as e:
        generate_log(text=str(e), log_type='ERROR')
        return None

def response_chat_qwen(model, prompt: str):
    try:
        response = model.create_chat_completion(
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=50
        )

        generate_log(text='Response LLM generated successfully.', log_type='SUCCESS')
        return response["choices"][0]["message"]["content"]
    except Ellipsis as e:
        generate_log(text=str(e), log_type='ERROR')
        return None
