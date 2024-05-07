# streamlit_app.py - Streamlit UI
import streamlit as st
import requests

def main():
    st.title("Text to Audio Converter")

    text = st.text_area("Enter the text:")
    audio_name = st.text_input("Enter the audio name to be saved:")

    if st.button("Convert to Audio"):
        if text and audio_name:
            data = {'text': text, 'audio_name': audio_name}
            response = requests.post('http://127.0.0.1:5000/convert-text-to-audio', json=data)
            if response.status_code == 200:
                st.success("Audio successfully created!")
            else:
                st.error("Error occurred during audio creation.")
        else:
            st.warning("Please enter both text and audio name.")

if __name__ == "__main__":
    main()
