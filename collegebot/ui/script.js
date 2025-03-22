document.getElementById('dark-mode-toggle').addEventListener('change', function() {
    if (this.checked) {
        document.body.classList.add('dark-mode');
        document.body.classList.remove('light-mode');
    } else {
        document.body.classList.add('light-mode');
        document.body.classList.remove('dark-mode');
    }
});

function createMessageElement(message, isUser) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user' : 'bot'}`;
    
    const content = document.createElement('div');
    content.className = 'message-content';
    content.textContent = message;
    
    messageDiv.appendChild(content);
    return messageDiv;
}

function sendMessage() {
    const input = document.getElementById('chat-input');
    const message = input.value.trim();
    
    if (message) {
        const chatBox = document.getElementById('chat-box');
        
        // Add user message
        chatBox.appendChild(createMessageElement(message, true));
        
        // Clear input
        input.value = '';
        
        // Simulate bot response (replace with actual API call)
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        })
        .then(response => response.json())
        .then(data => {
            const botResponse = data.response;
            chatBox.appendChild(createMessageElement(botResponse, false));
            chatBox.scrollTop = chatBox.scrollHeight;
        });
    }
}

function askQuestion(question) {
    document.getElementById('chat-input').value = question;
    sendMessage();
}

function startVoiceInput() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    const voiceButton = document.getElementById('voice-input-btn');
    
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    voiceButton.style.background = '#ff4444';
    recognition.start();

    recognition.onresult = function(event) {
        const input = document.getElementById('chat-input');
        input.value = event.results[0][0].transcript;
        voiceButton.style.background = '';
        sendMessage();
    };

    recognition.onerror = function(event) {
        console.error('Speech recognition error:', event.error);
        voiceButton.style.background = '';
    };

    recognition.onend = function() {
        voiceButton.style.background = '';
    };
}

// Add event listener for Enter key
document.getElementById('chat-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

// Initial welcome message
window.onload = function() {
    const chatBox = document.getElementById('chat-box');
    setTimeout(() => {
        chatBox.appendChild(createMessageElement('Hello! How can I assist you today?', false));
    }, 500);
};