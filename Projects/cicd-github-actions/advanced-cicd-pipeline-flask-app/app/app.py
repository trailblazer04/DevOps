from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)

# Configuration
app.config['VERSION'] = '1.0.0'
app.config['ENVIRONMENT'] = os.getenv('ENVIRONMENT', 'development')

# In-memory database (for demo purposes)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to CI/CD Demo API',
        'version': app.config['VERSION'],
        'environment': app.config['ENVIRONMENT'],
        'timestamp': datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()}), 200

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({'users': users, 'count': len(users)})

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400
    
    new_id = max(u['id'] for u in users) + 1 if users else 1
    new_user = {'id': new_id, 'name': data['name'], 'email': data['email']}
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = app.config['ENVIRONMENT'] == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)