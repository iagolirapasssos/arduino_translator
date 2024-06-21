from .commands import commands

class ArduinoTranslator:
    def __init__(self):
        self.commands = commands
    
    def translate(self, custom_code):
        arduino_code = custom_code
        for custom_command, arduino_command in self.commands.items():
            arduino_code = arduino_code.replace(custom_command, arduino_command)
        return arduino_code
