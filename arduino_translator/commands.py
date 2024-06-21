commands = {
    # Estruturas básicas
    'iniciar': {'translation': 'void setup()', 'category': 'function'},
    'loop': {'translation': 'void loop()', 'category': 'function'},
    
    # Funções de I/O digital
    'digitalEscrever': {'translation': 'digitalWrite', 'category': 'function'},
    'digitalLer': {'translation': 'digitalRead', 'category': 'function'},
    'pinoModo': {'translation': 'pinMode', 'category': 'function'},
    
    # Constantes
    'alta': {'translation': 'HIGH', 'category': 'keyword-other'},
    'baixa': {'translation': 'LOW', 'category': 'keyword-other'},
    'saida': {'translation': 'OUTPUT', 'category': 'keyword-other'},
    'entrada': {'translation': 'INPUT', 'category': 'keyword-other'},
    
    # Estruturas de controle
    'se': {'translation': 'if', 'category': 'conditional'},
    'senao': {'translation': 'else', 'category': 'conditional'},
    'para': {'translation': 'for', 'category': 'loop'},
    'enquanto': {'translation': 'while', 'category': 'loop'},
    'fazer': {'translation': 'do', 'category': 'loop'},
    'caso': {'translation': 'switch', 'category': 'conditional'},
    'casoDe': {'translation': 'case', 'category': 'conditional'},
    'quebrar': {'translation': 'break', 'category': 'conditional'},
    'continuar': {'translation': 'continue', 'category': 'conditional'},
    'retornar': {'translation': 'return', 'category': 'function'},
    
    # Tipos de dados
    'constante': {'translation': 'const', 'category': 'type'},
    'variavel': {'translation': 'int', 'category': 'type'},
    'flutuante': {'translation': 'float', 'category': 'type'},
    'caracter': {'translation': 'char', 'category': 'type'},
    'longo': {'translation': 'long', 'category': 'type'},
    'dobro': {'translation': 'double', 'category': 'type'},
    'semSinal': {'translation': 'unsigned', 'category': 'type'},
    'verdadeiro': {'translation': 'true', 'category': 'keyword-other'},
    'falso': {'translation': 'false', 'category': 'keyword-other'},
    'nada': {'translation': 'void', 'category': 'type'},
    'inteiro': {'translation': 'int', 'category': 'type'},
    'paraCada': {'translation': 'for each', 'category': 'loop'},
    
    # Funções de tempo
    'pausar': {'translation': 'delay', 'category': 'function'},
    'tempoAtual': {'translation': 'millis', 'category': 'function'},
    'tempoPassado': {'translation': 'micros', 'category': 'function'},
    
    # Funções de I/O analógico
    'pinoAnalogicoLer': {'translation': 'analogRead', 'category': 'function'},
    'pinoAnalogicoEscrever': {'translation': 'analogWrite', 'category': 'function'},
    
    # Funções de matemática
    'aleatorio': {'translation': 'random', 'category': 'function'},
    'aleatorioSeed': {'translation': 'randomSeed', 'category': 'function'},
    'mapear': {'translation': 'map', 'category': 'function'},
    
    # Funções de serial
    'conexaoSerial': {'translation': 'Serial.begin', 'category': 'function'},
    'imprimirSerial': {'translation': 'Serial.print', 'category': 'function'},
    'imprimirLinhaSerial': {'translation': 'Serial.println', 'category': 'function'},
    'disponivelSerial': {'translation': 'Serial.available', 'category': 'function'},
    'lerSerial': {'translation': 'Serial.read', 'category': 'function'},
    'escreverSerial': {'translation': 'Serial.write', 'category': 'function'},
    
    # Funções de interrupção
    'anexarInterrupcao': {'translation': 'attachInterrupt', 'category': 'function'},
    'desanexarInterrupcao': {'translation': 'detachInterrupt', 'category': 'function'},
    
    # Funções de som
    'inicioTons': {'translation': 'tone', 'category': 'function'},
    'pararTons': {'translation': 'noTone', 'category': 'function'},
    
    # Funções de pulso
    'lerPulso': {'translation': 'pulseIn', 'category': 'function'},
    
    # Operadores bitwise
    'eBitwise': {'translation': '&', 'category': 'keyword-other'},
    'ouBitwise': {'translation': '|', 'category': 'keyword-other'},
    'xorBitwise': {'translation': '^', 'category': 'keyword-other'},
    'notBitwise': {'translation': '~', 'category': 'keyword-other'},
    'shiftLeft': {'translation': '<<', 'category': 'keyword-other'},
    'shiftRight': {'translation': '>>', 'category': 'keyword-other'},
    
    # Classes
    'classe': {'translation': 'class', 'category': 'type'},
    'publico': {'translation': 'public', 'category': 'keyword-other'},
    'privado': {'translation': 'private', 'category': 'keyword-other'},
    'protegido': {'translation': 'protected', 'category': 'keyword-other'},
    'novo': {'translation': 'new', 'category': 'keyword-other'},
    
    # Funções adicionais
    'tamanho': {'translation': 'sizeof', 'category': 'function'},
    'tipoDef': {'translation': 'typedef', 'category': 'type'},
    'estruturar': {'translation': 'struct', 'category': 'type'},
    'enumerar': {'translation': 'enum', 'category': 'type'},
    'definir': {'translation': '#define', 'category': 'keyword-other'},
    'incluir': {'translation': '#include', 'category': 'keyword-other'},
    
    # Funções de controle avançado
    'retornarNada': {'translation': 'return void', 'category': 'function'},
    'externo': {'translation': 'extern', 'category': 'keyword-other'},
    'volatil': {'translation': 'volatile', 'category': 'keyword-other'},
    'registro': {'translation': 'register', 'category': 'keyword-other'},
    
    # Funções matemáticas adicionais
    'absoluto': {'translation': 'abs', 'category': 'function'},
    'constranho': {'translation': 'constrain', 'category': 'function'},
    'quadrado': {'translation': 'sq', 'category': 'function'},
    'raizQuadrada': {'translation': 'sqrt', 'category': 'function'},
    'minimo': {'translation': 'min', 'category': 'function'},
    'maximo': {'translation': 'max', 'category': 'function'},
    'valorIntermediario': {'translation': 'midpoint', 'category': 'function'},
    'potencia': {'translation': 'pow', 'category': 'function'},
    'logaritmo': {'translation': 'log', 'category': 'function'},
    'logaritmoNatural': {'translation': 'log10', 'category': 'function'},
    'exponencial': {'translation': 'exp', 'category': 'function'},
    'seno': {'translation': 'sin', 'category': 'function'},
    'cosseno': {'translation': 'cos', 'category': 'function'},
    'tangente': {'translation': 'tan', 'category': 'function'},
    
    # Outros
    'biblioteca': {'translation': '#include', 'category': 'keyword-other'},
    'definirConstante': {'translation': '#define', 'category': 'keyword-other'},
}