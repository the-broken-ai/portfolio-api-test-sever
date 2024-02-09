from flask import Flask, request, jsonify
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)
@app.route('/api/getdata', methods=['GET'])
def api():
    data = []
    for i in range(5):
        post = {
            'id': str(i+1),
            'title': 'title' + str(i+1),
            'github':'https://github.com/notsujansharma/js-insights',
            'username': 'user' + str(str(i+1)),
            'content': 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections ' + str(i+1),
        }
        data.append(post)
    return jsonify(data)

@app.route('/api/users/user3', methods=['GET'])
def user():
    return "abc"

if __name__ == '__main__':
    app.run(debug=True)