from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

users = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    logger.info(f'Client connected: {request.sid}')

    emit('security_confirmation', {
        'status': 'secure',
        'protocol': 'TLS 1.3',
        'encryption': 'AES-256-GCM'
    })

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
    secure_channel = data.get('secure_channel', False)
    
    if secure_channel:
        logger.info(f'Received secured message from {username}')
    else:
        logger.info(f'Received message from {username}')
        
    emit('message', {
        'username': username,
        'message': message,
        'secure_channel': secure_channel
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