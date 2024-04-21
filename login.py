#pip install Flask pymongo(as installed at time of database connection so not installed
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data (replace this with a proper database)
#users = {
    #'user1': 'password1',
    #'user2': 'password2'
#}

@app.route('/login', methods=['POST'])
def login():
    #auth = request.authorization

    #if not auth or not auth.username or not auth.password:
        #return jsonify({'message': 'Authorization required!'}), 401

    username = 'Rupsha'
    password = 'rupsh31'

    #if username in users and users[username] == password:
    if username=='Rupsha' and password=='rupsh31':
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Invalid username or password!'}), 401
def test():
    return 'test api created'
if __name__ == '__main__':
    app.run(debug=True)