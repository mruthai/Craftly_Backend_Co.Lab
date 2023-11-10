# __init__.py
from flask import Flask, render_template, redirect, url_for
from flask_socketio import SocketIO, emit
import os
from src.models.chat import Chat
from src.config import Config

app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app, logger=True, engineio_logger=True)

print(os.getenv("OPENAI_API_KEY"))
chat = Chat()

@app.route('/')
def home_page():
    """Render the home page."""
    return render_template('index.html')

@app.route('/refresh')
def refresh_history():
    """Clear the chat history."""
    chat.refresh_history()
    return redirect(url_for('home_page'))

@socketio.on('message')
def handle_message(data):
    """Handle a message sent by the user."""
    print(f"Received message: {data['data']}")
    response = chat.get_ai_answer(data['data'])
    emit('ai_answer', {'data': response}, broadcast=False)

if __name__ == '__main__':
    socketio.run(app)
