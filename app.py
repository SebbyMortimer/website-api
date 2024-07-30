import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, jsonify
import os
import base64
import json

app = Flask(__name__)

# Decode the Base64 encoded service account key
encoded_key = os.getenv('FIREBASE_SERVICE_ACCOUNT_KEY')
decoded_key = base64.b64decode(encoded_key).decode('utf-8')

# Load the decoded key into a dictionary
service_account_info = json.loads(decoded_key)

# Initialize the Firebase Admin SDK
cred = credentials.Certificate(service_account_info)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://website-api-project-3b792-default-rtdb.europe-west1.firebasedatabase.app/'
})

@app.route('/')
def home():
    return redirect(https://api.sebbymortimer.co.uk/docs)

@app.route('/docs')
def show_docs():
    return flask.render_template('docs/docs.html')

@app.route('/write/<user_id>/<name>', methods=['POST'])
def write_data(user_id, name):
    ref = db.reference(f'users/{user_id}')
    ref.set({
        'username': name
    })
    return jsonify(message="Data written successfully"), 200

@app.route('/read/<user_id>', methods=['GET'])
def read_data(user_id):
    ref = db.reference(f'users/{user_id}')
    snapshot = ref.get()
    if snapshot:
        return jsonify(username=snapshot['username']), 200
    else:
        return jsonify(error="User not found"), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
