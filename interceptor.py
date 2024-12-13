# interceptor.py
import socketio
from datetime import datetime
import base64

class ChatInterceptor:
    def __init__(self, server_url='http://localhost:5555'):
        self.sio = socketio.Client()
        self.server_url = server_url
        self.setup_handlers()
        
    def setup_handlers(self):
        @self.sio.on('connect')
        def on_connect():
            print(f'[{self.get_timestamp()}] Connected to server - intercepting messages...')
            
        @self.sio.on('message')
        def on_message(data):
            timestamp = self.get_timestamp()
            username = data.get('username', 'Unknown')
            message = data.get('message', '')
            is_encrypted = data.get('encrypted', False)
            
            # Try to decrypt if message is encrypted
            if is_encrypted:
                try:
                    decrypted_message = base64.b64decode(message).decode()
                    print(f'\n[{timestamp}] Intercepted encrypted message from {username}:')
                    print(f'  Encrypted: {message}')
                    print(f'  Decrypted: {decrypted_message}')
                    
                    # Log to file
                    with open('intercepted_messages.log', 'a') as log_file:
                        log_file.write(f'[{timestamp}] {username} (Encrypted):\n')
                        log_file.write(f'  Original: {message}\n')
                        log_file.write(f'  Decrypted: {decrypted_message}\n')
                        log_file.write('-' * 50 + '\n')
                except:
                    print(f'\n[{timestamp}] Failed to decrypt message from {username}: {message}')
            else:
                print(f'\n[{timestamp}] Intercepted message from {username}: {message}')
                # Log to file
                with open('intercepted_messages.log', 'a') as log_file:
                    log_file.write(f'[{timestamp}] {username}: {message}\n')
        
        @self.sio.on('system_message')
        def on_system_message(data):
            timestamp = self.get_timestamp()
            message = data.get('message', '')
            print(f'\n[{timestamp}] System Message: {message}')
                
    def get_timestamp(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
    def start_intercepting(self):
        try:
            print(f'[{self.get_timestamp()}] Starting interceptor...')
            self.sio.connect(self.server_url)
            self.sio.wait()
        except Exception as e:
            print(f'Error: {e}')
        finally:
            if self.sio.connected:
                self.sio.disconnect()

if __name__ == '__main__':
    interceptor = ChatInterceptor()
    interceptor.start_intercepting()