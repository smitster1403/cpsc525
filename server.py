# server.py
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Store active users
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    logger.info(f'Client connected: {request.sid}')

@socketio.on('join')
def handle_join(data):
    username = data.get('username', 'Anonymous')
    users[request.sid] = username
    join_message = f'{username} has joined the chat'
    logger.info(join_message)
    emit('system_message', {'message': join_message}, broadcast=True)

@socketio.on('message')
def handle_message(data):
    username = users.get(request.sid, 'Anonymous')
    message = data.get('message', '')
    
    # Simply pass the message along - no encryption
    logger.info(f'Message from {username}: {message}')
    emit('message', {
        'username': username,
        'message': message
    }, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in users:
        username = users[request.sid]
        leave_message = f'{username} has left the chat'
        logger.info(leave_message)
        del users[request.sid]
        emit('system_message', {'message': leave_message}, broadcast=True)

if __name__ == '__main__':
    logger.info("Starting server on port 5555")
    socketio.run(app, host='0.0.0.0', port=5555, debug=True)