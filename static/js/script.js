function initializeEditor(keywords) {
    let customKeywords = {};
    for (const keyword in keywords) {
        let category = keywords[keyword];
        customKeywords[keyword] = `keyword-${category}`;
    }

    CodeMirror.defineMIME("text/x-custom", {
        name: "clike",
        keywords: customKeywords
    });

    let editor = CodeMirror.fromTextArea(document.getElementById('editor-textarea'), {
        lineNumbers: true,
        mode: "text/x-custom",
        theme: "darcula"
    });

    let translation = CodeMirror.fromTextArea(document.getElementById('translation-textarea'), {
        lineNumbers: true,
        mode: "text/x-c++src",
        theme: "darcula",
        readOnly: true
    });

    editor.on('change', function() {
        updateTranslation(editor, translation);
    });

    return { editor, translation };
}

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

function newFile(editor, translation) {
    editor.setValue('');
    translation.setValue('');
}

function openFile(editor) {
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

function saveFile(editor) {
    let content = editor.getValue();
    let blob = new Blob([content], { type: 'text/plain' });
    let url = URL.createObjectURL(blob);
    let a = document.createElement('a');
    a.href = url;
    a.download = 'code.pyno';
    a.click();
    URL.revokeObjectURL(url);
}

function saveFileAs(editor) {
    let content = editor.getValue();
    let blob = new Blob([content], { type: 'text/plain' });
    let url = URL.createObjectURL(blob);
    let a = document.createElement('a');
    a.href = url;
    a.download = prompt('Nome do arquivo', 'code.pyno');
    a.click();
    URL.revokeObjectURL(url);
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

function showShortcuts() {
    alert('Atalhos: \nNovo: Ctrl+N \nAbrir: Ctrl+O \nSalvar: Ctrl+S \nSalvar Como: Ctrl+Shift+S \nTraduzir: Ctrl+T');
}

document.addEventListener('DOMContentLoaded', (event) => {
    fetchKeywordsAndInitializeEditor();
});
