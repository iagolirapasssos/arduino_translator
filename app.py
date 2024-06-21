from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from arduino_translator.translator import ArduinoTranslator
import os

app = Flask(__name__)
CORS(app, resources={r"/translate": {"origins": "*"}})

translator = ArduinoTranslator()

@app.route('/translate', methods=['POST'])
def translate_code():
    data = request.json
    custom_code = data['code']
    arduino_code = translator.translate(custom_code)

    with open('translated.ino', 'w') as f:
        f.write(arduino_code)

    return send_file('translated.ino', as_attachment=True, download_name='translated.ino')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
