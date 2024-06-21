# Arduino Translator

Arduino Translator é uma ferramenta para traduzir uma linguagem personalizada de comandos para código Arduino.

## Instalação

Você pode instalar o Arduino Translator usando `pip`:

```sh
pip install git+https://github.com/seu_usuario/arduino_translator.git
```

## Uso

Para usar o tradutor, execute o seguinte comando no terminal:

```sh
arduino-translate input_file output_file
```

Onde `input_file` é o arquivo contendo o código personalizado e `output_file` é o arquivo onde o código Arduino traduzido será salvo.
```

#### 6. `.gitignore`
```
*.pyc
__pycache__/
*.pyo
*.pyd
.env
```

#### 7. `requirements.txt`
```
# Lista de dependências
```

### Subindo para o GitHub

1. **Inicializar um repositório Git:**
    ```sh
    git init
    git add .
    git commit -m "Initial commit"
    ```

2. **Criar um novo repositório no GitHub.**

3. **Adicionar o repositório remoto e enviar o código:**
    ```sh
    git remote add origin https://github.com/seu_usuario/arduino_translator.git
    git branch -M main
    git push -u origin main
    ```

Agora, o tradutor está pronto para ser usado e pode ser instalado via `pip` diretamente do GitHub. Este projeto permite a tradução de uma linguagem personalizada para comandos da linguagem Arduino, facilitando o desenvolvimento de programas para Arduino em uma linguagem mais familiar.

Para incluir exemplos de uso no projeto, podemos criar uma pasta chamada `examples` e adicionar alguns arquivos de exemplo que demonstram como usar o tradutor. Vamos estruturar essa pasta e fornecer alguns exemplos.

### Estrutura do Projeto Atualizada

1. **Diretório do Projeto:**
    - `arduino_translator/`
        - `__init__.py`
        - `translator.py`
        - `cli.py`
    - `examples/`
        - `example1.txt`
        - `example2.txt`
        - `example_translated1.ino`
        - `example_translated2.ino`
    - `setup.py`
    - `README.md`
    - `.gitignore`
    - `requirements.txt`

### Conteúdo da Pasta `examples`

#### 1. `examples/example1.txt`
```plaintext
iniciar {
    pinoModo(13, saida);
}

loop {
    digitalEscrever(13, alta);
    delay(1000);
    digitalEscrever(13, baixa);
    delay(1000);
}
```

#### 2. `examples/example2.txt`
```plaintext
iniciar {
    pinoModo(7, entrada);
    pinoModo(13, saida);
}

loop {
    int valor = digitalLer(7);
    if (valor == alta) {
        digitalEscrever(13, alta);
    } else {
        digitalEscrever(13, baixa);
    }
}
```

#### 3. `examples/example_translated1.ino`
```cpp
void setup() {
    pinMode(13, OUTPUT);
}

void loop() {
    digitalWrite(13, HIGH);
    delay(1000);
    digitalWrite(13, LOW);
    delay(1000);
}
```

#### 4. `examples/example_translated2.ino`
```cpp
void setup() {
    pinMode(7, INPUT);
    pinMode(13, OUTPUT);
}

void loop() {
    int valor = digitalRead(7);
    if (valor == HIGH) {
        digitalWrite(13, HIGH);
    } else {
        digitalWrite(13, LOW);
    }
}
```

# Arduino Translator

Arduino Translator é uma ferramenta para traduzir uma linguagem personalizada de comandos para código Arduino.

## Instalação

Você pode instalar o Arduino Translator usando `pip`:

```sh
pip install git+https://github.com/seu_usuario/arduino_translator.git
```

## Uso

Para usar o tradutor, execute o seguinte comando no terminal:

```sh
arduino-translate input_file output_file
```

Onde `input_file` é o arquivo contendo o código personalizado e `output_file` é o arquivo onde o código Arduino traduzido será salvo.

## Exemplos

Veja a pasta `examples` para alguns exemplos de uso:

- `example1.txt` contém um exemplo de código personalizado.
- `example_translated1.ino` contém o código traduzido para Arduino.
- `example2.txt` contém outro exemplo de código personalizado.
- `example_translated2.ino` contém o código traduzido para Arduino.

Para traduzir um exemplo:

```sh
arduino-translate examples/example1.txt examples/example_translated1.ino
```
```

### Subindo as Mudanças para o GitHub

1. **Adicionar os novos arquivos e exemplos:**
    ```sh
    git add .
    git commit -m "Added examples of usage"
    ```

2. **Enviar as mudanças para o repositório remoto:**
    ```sh
    git push
    ```

Com essas alterações, o projeto agora inclui exemplos de uso que demonstram como utilizar o tradutor. Os usuários podem consultar a pasta `examples` para ver exemplos de código personalizado e o código Arduino resultante após a tradução.