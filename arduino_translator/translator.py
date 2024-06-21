import re
from .commands import commands

class ArduinoTranslator:
    def __init__(self):
        self.commands = commands
    
    def translate(self, custom_code):
        arduino_code = custom_code
        for custom_command, details in self.commands.items():
            arduino_command = details['translation']
            # Usando regex para substituir apenas palavras completas
            arduino_code = re.sub(r'\b' + re.escape(custom_command) + r'\b', arduino_command, arduino_code)
        return arduino_code
