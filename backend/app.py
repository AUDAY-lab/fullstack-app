from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# MongoDB setup
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/student_db')
client = MongoClient(MONGO_URI)
db = client.student_db
users = db.users

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Backend is running!'})

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        
        if not name or not email:
            return jsonify({'error': 'Name and email are required'}), 400
        
        # Save to MongoDB
        user_data = {
            'name': name,
            'email': email
        }
        users.insert_one(user_data)
        
        print(f"New user added: {name} - {email}")
        return jsonify({'message': 'User saved successfully!'})
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Failed to save user'}), 500

@app.route('/users', methods=['GET'])
def get_users():
    try:
        all_users = list(users.find({}, {'_id': 0}))
        print(f"Total users in database: {len(all_users)}")
        for user in all_users:
            print(f"- {user['name']} ({user['email']})")
        return jsonify({'users': all_users})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Failed to fetch users'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)