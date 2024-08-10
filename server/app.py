from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid 

#onstantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS 
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route 
@app.route('/ping', methods=['GET'])
def ping_pong(): 
    return jsonify('datos random') 

if __name__ == '__main__': 
    app.run(port=5001, debug=True)

#Router handler for Books component 
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST': 
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid5().hex, 
            'title': post_data.get('title'), 
            'author': post_data.get('author'), 
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else: 
        response_object['books'] = BOOKS 
    return jsonify(response_object) 


BOOKS = [
    {   'id': uuid.uuid4().hex, 
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {   'id': uuid.uuid4().hex, 
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {   
        'id': uuid.uuid4().hex, 
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


