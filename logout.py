from flask import Flask, request, jsonify

app = Flask(__name__)

# Example user session data (replace this with your actual session management)
active_sessions = {}

@app.route('/logout', methods=['POST'])
def logout():
    # Get the token or session ID from the request
    token = request.json.get('token')

    if token:
        # Invalidate the session/token
        active_sessions.pop(token, None)
        return jsonify({'message': 'Logout successful'})
    else:
        return jsonify({'error': 'Token is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)