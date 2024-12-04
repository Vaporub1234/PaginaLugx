// Mostrar u ocultar el chat
function toggleChat() {
  const chatContainer = document.getElementById('chatContainer');
  chatContainer.classList.toggle('hidden');
}

// Enviar mensaje al backend y obtener la respuesta
function sendMessage() {
  const userMessage = document.getElementById('userMessage').value.trim();
  if (userMessage === "") return;

  // Mostrar mensaje del usuario en el chat
  displayMessage("Tú: " + userMessage);

  // Limpiar el campo de entrada
  document.getElementById('userMessage').value = "";

  // Enviar el mensaje al backend
  fetch('http://localhost:8080', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: userMessage })
  })
  .then(response => response.json())
  .then(data => {
      displayMessage("Chatbot: " + data.response);
  })
  .catch(error => {
      displayMessage("Chatbot: Lo siento, algo salió mal.");
  });
}

// Mostrar mensajes en el chat
function displayMessage(message) {
  const chatMessages = document.getElementById('chatMessages');
  const messageElement = document.createElement('div');
  messageElement.textContent = message;
  chatMessages.appendChild(messageElement);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}
