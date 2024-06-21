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

Agora, o tradutor está pronto para ser usado e pode ser instalado via `pip` diretamente do GitHub. Este projeto permite a tradução de uma linguagem personalizada para comandos da linguagem Arduino, facilitando o desenvolvimento de programas para Arduino em uma linguagem mais familiar.


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