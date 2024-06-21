import argparse
from .translator.py import ArduinoTranslator

def main():
    parser = argparse.ArgumentParser(description='Translate custom Arduino language to Arduino code.')
    parser.add_argument('input_file', help='Input file containing custom Arduino code')
    parser.add_argument('output_file', help='Output file for the translated Arduino code')

    args = parser.parse_args()

    with open(args.input_file, 'r') as f:
        custom_code = f.read()

    translator = ArduinoTranslator()
    arduino_code = translator.translate(custom_code)

    with open(args.output_file, 'w') as f:
        f.write(arduino_code)

if __name__ == '__main__':
    main()