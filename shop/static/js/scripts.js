//Aqui eu começo o script de reconhecimento de voz
window.addEventListener('DOMContentLoaded', function() {
    var speakBtn = document.querySelector('#search-field');

    // testa se o navegador suporta o reconhecimento de voz
    if (window.SpeechRecognition || window.webkitSpeechRecognition) {

        // captura a voz
        var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;

        var recognition = new SpeechRecognition();

        // inicia reconhecimento
        speakBtn.addEventListener('click', function(e) {
            recognition.start();
        }, false);

        // resultado do reconhecimento
        recognition.addEventListener('result', function(e) {
            console.log(e);
            var result = e.results[0][0].transcript;
            console.log(result);
            document.getElementById('search-field').value = result;
            document.getElementById('form-pesquisar').submit();
        }, false);
    } else {
        //Funciona somente no google chrome
    }
}, false);
