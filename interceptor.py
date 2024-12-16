import socketio
from datetime import datetime

class ChatInterceptor:
    def __init__(self, server_url='http://localhost:5555'):
        self.sio = socketio.Client()
        self.server_url = server_url
        self.setup_handlers()
        
    def setup_handlers(self):
        @self.sio.on('connect')
        def on_connect():
            print(f'[{self.get_timestamp()}] Connected to server - intercepting messages...')
        
        @self.sio.on('security_confirmation')
        def on_security(data):
            print(f"\n[{self.get_timestamp()}] Intercepted security confirmation:")
            print(f"Claimed security status: {data.get('status')}")
            print(f"Claimed protocol: {data.get('protocol')}")
            print(f"Claimed encryption: {data.get('encryption')}")
            
        @self.sio.on('message')
        def on_message(data):
            timestamp = self.get_timestamp()
            username = data.get('username', 'Unknown')
            message = data.get('message', '')
            secure_channel = data.get('secure_channel', False)
            
    
            print(f'\n[{timestamp}] Intercepted message from {username}: {message}')
            
            with open('intercepted_messages.log', 'a') as log_file:
                log_file.write(f'[{timestamp}] {username} {"(Claims Secure)" if secure_channel else ""}: {message}\n')
        
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