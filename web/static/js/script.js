let editor = CodeMirror.fromTextArea(document.getElementById('editor'), {
    lineNumbers: true,
    mode: "text/x-csrc",
    theme: "darcula"
});

function newFile() {
    editor.setValue('');
}

function openFile() {
    let input = document.createElement('input');
    input.type = 'file';
    input.accept = '.pyno';
    input.onchange = e => { 
        let file = e.target.files[0]; 
        let reader = new FileReader();
        reader.onload = e => { 
            editor.setValue(e.target.result);
        };
        reader.readAsText(file);
    };
    input.click();
}

function saveFile() {
    let content = editor.getValue();
    let blob = new Blob([content], { type: 'text/plain' });
    let url = URL.createObjectURL(blob);
    let a = document.createElement('a');
    a.href = url;
    a.download = 'code.pyno';
    a.click();
    URL.revokeObjectURL(url);
}

function saveFileAs() {
    let content = editor.getValue();
    let blob = new Blob([content], { type: 'text/plain' });
    let url = URL.createObjectURL(blob);
    let a = document.createElement('a');
    a.href = url;
    a.download = prompt('Nome do arquivo', 'code.pyno');
    a.click();
    URL.revokeObjectURL(url);
}

function translateCode() {
    let content = editor.getValue();
    fetch('http://162.248.101.160:5000/translate', { // Atualize com o IP correto da sua VPS
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

function showShortcuts() {
    alert('Atalhos: \nNovo: Ctrl+N \nAbrir: Ctrl+O \nSalvar: Ctrl+S \nSalvar Como: Ctrl+Shift+S \nTraduzir: Ctrl+T');
}
