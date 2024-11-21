from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
# here is a template
# Simulated encryption state
encryption_enabled = False
@app.route('/favicon.ico')
def favicon():
    return '', 204  # No content for favicon

@app.route('/')
def home():
    return render_template('index.html')  # Serve the frontend HTML file

@app.route('/toggle-encryption', methods=['POST'])
def toggle_encryption():
    global encryption_enabled
    # Read the user input from the request
    enable_encryption = request.json.get('enableEncryption', False)
    if enable_encryption:
        encryption_enabled = False  # Vulnerability: Intentionally do not enable encryption
    else:
        encryption_enabled = False
    return jsonify({"message": "Encryption status updated", "encryptionEnabled": encryption_enabled})

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"encryptionEnabled": encryption_enabled})

if __name__ == "__main__":
    app.run(debug=True)
