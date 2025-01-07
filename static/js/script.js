// const chatArea = document.getElementById('chat-area');
// const userInput = document.getElementById('user-input');
// const sendBtn = document.getElementById('send-btn');

// function addMessage(message, isBot = false) {
//     const messageDiv = document.createElement('div');
//     messageDiv.className = `message ${isBot ? 'bot-message' : 'user-message'}`;
    
//     if (isBot) {
//         const botIcon = document.createElement('span');
//         botIcon.className = 'bot-icon';
//         botIcon.textContent = '🤖';
//         messageDiv.appendChild(botIcon);
//     }
    
//     messageDiv.appendChild(document.createTextNode(message));
//     chatArea.appendChild(messageDiv);
//     chatArea.scrollTop = chatArea.scrollHeight;
// }

// async function handleSend() {
//     const message = userInput.value.trim();
//     if (message) {
//         addMessage(message);
//         userInput.value = '';
        
//         try {
//             const response = await fetch('/ask', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify({ question: message })
//             });
            
//             const data = await response.json();
//             addMessage(data.answer, true);
            
//         } catch (error) {
//             console.error('Error:', error);
//             addMessage('Sorry, there was an error processing your question.', true);
//         }
//     }
// }

// sendBtn.addEventListener('click', handleSend);
// userInput.addEventListener('keypress', (e) => {
//     if (e.key === 'Enter') {
//         handleSend();
//     }
// });


// const chatArea = document.getElementById('chat-area');
// const userInput = document.getElementById('user-input');
// const sendBtn = document.getElementById('send-btn');

// function addMessage(message, isBot = false) {
//     const messageDiv = document.createElement('div');
//     messageDiv.className = `message ${isBot ? 'bot-message' : 'user-message'}`;
    
//     if (isBot) {
//         const botIcon = document.createElement('span');
//         botIcon.className = 'bot-icon';
//         botIcon.textContent = '🤖';
//         messageDiv.appendChild(botIcon);
//     }
    
//     messageDiv.appendChild(document.createTextNode(message));
//     chatArea.appendChild(messageDiv);
//     chatArea.scrollTop = chatArea.scrollHeight;
// }

// async function handleSend() {
//     const message = userInput.value.trim();
//     if (message) {
//         addMessage(message);
//         userInput.value = '';
        
//         try {
//             const response = await fetch('/ask', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify({ question: message })
//             });
            
//             const data = await response.json();
//             addMessage(data.answer, true);
//         } catch (error) {
//             console.error('Error:', error);
//             addMessage('Sorry, there was an error processing your question.', true);
//         }
//     }
// }

// sendBtn.addEventListener('click', handleSend);
// userInput.addEventListener('keypress', (e) => {
//     if (e.key === 'Enter') {
//         handleSend();
//     }
// });


const chatArea = document.getElementById('chat-area');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

function addMessage(message, isBot = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isBot ? 'bot-message' : 'user-message'}`;
    
    if (isBot) {
        const botIcon = document.createElement('span');
        botIcon.className = 'bot-icon';
        botIcon.textContent = '🤖';
        messageDiv.appendChild(botIcon);
    }
    
    messageDiv.appendChild(document.createTextNode(message));
    chatArea.appendChild(messageDiv);
    chatArea.scrollTop = chatArea.scrollHeight;
}

async function handleSend() {
    const message = userInput.value.trim();
    if (message) {
        addMessage(message);
        userInput.value = '';
        
        try {
            const response = await fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question: message })
            });
            
            const data = await response.json();
            addMessage(data.answer, true);
        } catch (error) {
            console.error('Error:', error);
            addMessage('Sorry, there was an error processing your question.', true);
        }
    }
}

sendBtn.addEventListener('click', handleSend);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleSend();
    }
});