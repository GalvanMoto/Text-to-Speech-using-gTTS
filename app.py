# app.py - Flask API
from flask import Flask, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/convert-text-to-audio', methods=['POST'])
def convert_text_to_audio():
    data = request.get_json()
    if 'text' not in data or 'audio_name' not in data:
        return jsonify({'error': 'Text and audio_name are required fields.'}), 400

    text = data['text']
    audio_name = data['audio_name']

    # Create the 'audio' directory if it doesn't exist
    if not os.path.exists('audio'):
        os.makedirs('audio')

    tts = gTTS(text=text, lang='en', slow=False)
    audio_file_path = os.path.join('audio', f'{audio_name}.mp3')
    tts.save(audio_file_path)

    return jsonify({'message': f'Audio saved as {audio_name}.mp3'}), 200

if __name__ == '__main__':
    app.run(debug=True)
