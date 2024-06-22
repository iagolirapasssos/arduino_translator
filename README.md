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

### Configuração do Nginx para SSL

Certifique-se de que o Nginx está configurado corretamente para usar os certificados SSL e redirecionar todo o tráfego HTTP para HTTPS.

#### `/etc/nginx/sites-available/arduino_translator`

```nginx
server {
    listen 80;
    server_name bosonshiggs.com.br www.bosonshiggs.com.br;

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name bosonshiggs.com.br www.bosonshiggs.com.br;

    ssl_certificate /etc/letsencrypt/live/bosonshiggs.com.br/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/bosonshiggs.com.br/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        proxy_pass http://127.0.0.1:5000;  # Proxy pass to HTTP
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Configuração do Gunicorn para HTTP

Mantenha o Gunicorn servindo via HTTP, sem configurar SSL diretamente no Gunicorn. A configuração do Gunicorn deve ser simples:

#### `gunicorn_config.py`

```python
bind = "0.0.0.0:5000"
workers = 4
```

### Reiniciar Nginx e Gunicorn

Reinicie o Nginx para aplicar as mudanças:

```sh
sudo systemctl restart nginx
```

Execute o Gunicorn novamente para garantir que ele está funcionando:

```sh
source venv/bin/activate
gunicorn -c gunicorn_config.py app:app
```

### Verificar Logs

Verifique os logs do Nginx e Gunicorn para garantir que não há erros adicionais.

#### Verificar Logs do Nginx

```sh
sudo tail -f /var/log/nginx/error.log
```

#### Verificar Logs do Gunicorn

```sh
sudo tail -f /var/log/gunicorn.log
```

### Testar o Acesso ao Site

Após essas alterações, o servidor Flask deve estar configurado para servir via HTTPS, e todas as solicitações do frontend devem ser feitas para o novo domínio. Abra a página no navegador através do domínio `https://bosonshiggs.com.br` e verifique se a comunicação com o servidor Flask está funcionando corretamente e se a tradução está sendo atualizada em tempo real.

### Implementando mais de uma API com o mesmo IP

Para configurar isso, você pode usar o Nginx como um proxy reverso para redirecionar as solicitações para diferentes servidores ou instâncias de aplicação com base no caminho da URL.

### Exemplo de Configuração

Vamos supor que você tem duas APIs:

1. **API1** servida por Gunicorn no endereço `http://127.0.0.1:5000`
2. **API2** servida por Gunicorn no endereço `http://127.0.0.1:6000`

Você pode configurar o Nginx para redirecionar as solicitações para diferentes APIs com base no caminho da URL. Por exemplo, todas as solicitações para `https://bosonshiggs.com.br/api1/` serão redirecionadas para a API1 e todas as solicitações para `https://bosonshiggs.com.br/api2/` serão redirecionadas para a API2.

### Configuração do Nginx

#### `/etc/nginx/sites-available/bosonshiggs`

```nginx
server {
    listen 80;
    server_name bosonshiggs.com.br www.bosonshiggs.com.br;

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name bosonshiggs.com.br www.bosonshiggs.com.br;

    ssl_certificate /etc/letsencrypt/live/bosonshiggs.com.br/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/bosonshiggs.com.br/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location /api1/ {
        proxy_pass http://127.0.0.1:5000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /api2/ {
        proxy_pass http://127.0.0.1:6000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Configuração do Gunicorn

Certifique-se de que ambas as instâncias do Gunicorn estão executando nas portas corretas.

#### API1

Inicie o Gunicorn para a API1 na porta 5000:

```sh
gunicorn -b 127.0.0.1:5000 app1:app
```

#### API2

Inicie o Gunicorn para a API2 na porta 6000:

```sh
gunicorn -b 127.0.0.1:6000 app2:app
```

### Atualização do Frontend

Certifique-se de que o frontend está configurado para fazer solicitações para os caminhos corretos das APIs.

#### `web/static/js/script.js`

```javascript
function fetchKeywordsAndInitializeEditor() {
    fetch('https://bosonshiggs.com.br/api1/keywords')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(keywords => {
            let { editor, translation } = initializeEditor(keywords);

            document.querySelector('.menu-item[onclick="newFile()"]').onclick = () => newFile(editor, translation);
            document.querySelector('.menu-item[onclick="openFile()"]').onclick = () => openFile(editor);
            document.querySelector('.menu-item[onclick="saveFile()"]').onclick = () => saveFile(editor);
            document.querySelector('.menu-item[onclick="saveFileAs()"]').onclick = () => saveFileAs(editor);
            document.querySelector('.menu-item[onclick="translateCode()"]').onclick = () => translateCode(editor);
        })
        .catch(error => {
            console.error('Erro ao buscar palavras reservadas:', error);
        });
}

function updateTranslation(editor, translation) {
    let content = editor.getValue();
    fetch('https://bosonshiggs.com.br/api1/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: content })
    })
    .then(response => response.text())
    .then(translatedCode => {
        translation.setValue(translatedCode);
    })
    .catch(error => {
        console.error('Erro na tradução:', error);
    });
}

function translateCode(editor) {
    let content = editor.getValue();
    fetch('https://bosonshiggs.com.br/api1/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: content })
    })
    .then(response => response.blob())
    .then(blob => {
        let url = URL.createObjectURL(blob);
        let a = document.createElement('a');
        a.href = url;
        a.download = 'translated.ino';
        a.click();
        URL.revokeObjectURL(url);
    })
    .catch(error => {
        console.error('Erro na tradução:', error);
    });
}

document.addEventListener('DOMContentLoaded', (event) => {
    fetchKeywordsAndInitializeEditor();
});
```

### Commit e Push das Alterações

1. **Commit e Push das alterações no `script.js`:**

```sh
git add static/js/script.js
git commit -m "Update URLs to use new paths for APIs"
git push origin web
```

### Reiniciar o Nginx

Reinicie o Nginx para aplicar as mudanças:

```sh
sudo systemctl restart nginx
```

### Testar o Acesso ao Site

Após essas alterações, abra a página no navegador através do domínio `https://bosonshiggs.com.br` e verifique se a comunicação com ambas as APIs está funcionando corretamente e se a tradução está sendo atualizada em tempo real.

Com essas alterações, o projeto agora inclui exemplos de uso que demonstram como utilizar o tradutor. Os usuários podem consultar a pasta `examples` para ver exemplos de código personalizado e o código Arduino resultante após a tradução.