document.addEventListener('DOMContentLoaded', () => {
    const chatWindow = document.getElementById('chat-window');
    const chatInput = document.getElementById('chat-input');
    const sendBtn = document.getElementById('send-btn');

    // Utility to add message to UI
    function addMessage(text, sender) {
        const msgDiv = document.createElement('div');
        msgDiv.classList.add('chat-bubble', sender, 'shadow-sm', 'opacity-0', 'transition-opacity', 'duration-300');
        msgDiv.textContent = text;
        chatWindow.appendChild(msgDiv);
        
        // Scroll to bottom
        chatWindow.scrollTop = chatWindow.scrollHeight;
        
        // Setup fade-in animation
        requestAnimationFrame(() => {
            msgDiv.classList.remove('opacity-0');
        });
    }

    // Handle send event
    async function sendMessage() {
        const text = chatInput.value.trim();
        if (!text) return;

        // 1. Add User Message
        addMessage(text, 'user');
        chatInput.value = '';
        chatInput.focus();

        // 2. Add temporary typing indicator
        const typingDiv = document.createElement('div');
        typingDiv.classList.add('chat-bubble', 'bot', 'shadow-sm', 'text-slate-400', 'italic', 'text-sm');
        typingDiv.id = 'typing-indicator';
        typingDiv.textContent = 'Typing...';
        chatWindow.appendChild(typingDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;

        try {
            // 3. Make API request
            const response = await API.post('/chatbot/ask', { message: text });
            
            // 4. Remove typing indicator and add Bot response
            typingDiv.remove();
            addMessage(response.reply, 'bot');
            
        } catch (error) {
            console.error('Chatbot API Error:', error);
            typingDiv.remove();
            addMessage('Sorry, I am having trouble connecting to the server. Please try again later.', 'bot');
        }
    }

    // Event listeners
    sendBtn.addEventListener('click', sendMessage);
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Auto-focus input on load
    chatInput.focus();
});
