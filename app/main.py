
import streamlit as st
import requests as rq

URL = 'http://127.0.0.1:5000/predict'

st.title('🎉 Taxi Predict')
st.write('*With ML, LLM, TTS and API Based.*')

form_predict = st.form('form_predict', border=False)
distance = float(form_predict.text_input(label='Distance:', value=5.6))
traffic = int(form_predict.text_input(label='Traffic:', value=2))

submited = form_predict.form_submit_button()
if submited:
    with st.spinner(show_time=True):
        response = rq.post(url=URL, json={"distance": distance, "traffic": traffic})
        
    try:
        st.toast(body=response.json()['data']['message'], duration=2)

        st.write('Response Predict:')
        st.write(f'## {response.json()['data']['response_predict']} IRR')
        st.divider()
        st.write('Response LLM:')
        st.write(f'### {response.json()['data']['response_llm']}')
        
        st.write('Response TTS:')
        st.audio(data=response.json()['data']['response_tts'], autoplay=True)
    except Exception as e:
        st.error(body=str(e))
