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
            if (result.toLowerCase() === 'fazer login' || result.toLowerCase() === 'usuário') {
                  document.getElementById('link-usuario').click();
            }else if(result.toLowerCase() === 'home' || result.toLowerCase() === 'principal'){
                  document.getElementById('link-home').click();
            }else if(result.toLowerCase() === 'admin' || result.toLowerCase() === 'administrador'){
                  document.getElementById('link-admin').click();
            }else if(result.toLowerCase() === 'sobre'){
                  document.getElementById('link-sobre').click();
            }else if(result.toLowerCase() === 'sair'){
                  document.getElementById('link-sair').click();
            }else{
              document.getElementById('form-pesquisar').submit();
            }
        }, false);
    } else {
        //Funciona somente no google chrome
    }
}, false);
