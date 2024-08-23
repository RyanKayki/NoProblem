let isSpeaking = false;

function speakText() {
    const responseElement = document.getElementById('response');
    const text = responseElement.innerText || responseElement.textContent;
    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = 'pt-BR';

    if (isSpeaking) {
        window.speechSynthesis.cancel(); // Para a leitura se estiver em andamento
        isSpeaking = false;
        toggleVolumeIcon('mute');
    } else {
        window.speechSynthesis.speak(speech);
        isSpeaking = true;
        toggleVolumeIcon('off');
    }
}

function toggleVolumeIcon(state) {
    const muteIcon = document.querySelector('.fa-volume-mute');
    const volumeOffIcon = document.querySelector('.fa-volume-off');
    const volumeUpIcon = document.querySelector('.fa-volume-up');

    if (state === 'mute') {
        muteIcon.style.display = 'block';
        volumeOffIcon.style.display = 'none';
        volumeUpIcon.style.display = 'none';
    } else if (state === 'off') {
        muteIcon.style.display = 'none';
        volumeOffIcon.style.display = 'block';
        volumeUpIcon.style.display = 'none';
    } else if (state === 'up') {
        muteIcon.style.display = 'none';
        volumeOffIcon.style.display = 'none';
        volumeUpIcon.style.display = 'block';
    }
}

// Inicialmente, defina o ícone como mute
toggleVolumeIcon('mute');

// Exibe o botão de leitura após a resposta ser gerada
function showSpeakButton() {
    document.getElementById('speakButton').style.display = 'block';
}

// Atualiza o nome da função para evitar conflito
function handleResponseAndShowButton() {
    // Aqui você faz o submit dos dados e recebe a resposta.
    // Após receber a resposta e atualizar o conteúdo do <div> com id="response",
    // chame a função showSpeakButton()
    showSpeakButton();
}