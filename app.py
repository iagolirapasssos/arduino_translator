from flask import Flask, request, jsonify, send_file
from arduino_translator.translator import ArduinoTranslator
import os

app = Flask(__name__)

translator = ArduinoTranslator()

@app.route('/translate', methods=['POST'])
def translate_code():
    data = request.json
    custom_code = data['code']
    arduino_code = translator.translate(custom_code)

    with open('translated.ino', 'w') as f:
        f.write(arduino_code)

    return send_file('translated.ino', as_attachment=True, attachment_filename='translated.ino')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
