from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongodb:27017/webappdb'  # 'mongodb' is the service name defined in docker-compose.yml
mongo = PyMongo(app)

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    mongo.db.users.insert_one({'name': name, 'email': email})
    return jsonify({'message': 'Data stored successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
