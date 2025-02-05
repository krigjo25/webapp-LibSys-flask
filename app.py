# Entry point for the application


import uuid as ID

# Importing the required libraries
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_session import Session
from flask_cors import CORS



#   Import application repositories
from lib.config.config import DevelopmentConfig

#   Import the application views
from lib.views.index import BookShelf

#   Load the environment variables from the .env file
load_dotenv()

app = Flask(__name__)

#   Load the configuration settings for the app
app.config.from_object(DevelopmentConfig)
Session(app)

#   Enable the CORS for the application
CORS(app, resources={r"/*": {"origins": "*"}})


#   Application webworkers

@app.after_request
def after_request(response):
    """ Ensures that the responses are not cached """

    response.headers['Expires'] = 0
    response.headers['Pragma'] = "no-cache"
    response.headers['Cache-Control'] = "no-cache, no-store, must-revalidate"
    return response


Books = [
    {
        'id': ID.uuid4().hex,
        'title': 'The Alchemist',
        'author': 'Paulo Coelho',
        'read': True
    },
    {
        'id': ID.uuid4().hex,
        'title': 'The Secret',
        'author': 'Rhonda Byrne',
        'read': False
    }
]

@app.route('/', methods=['GET', 'POST'])
def get_books():
    response = {"status": "success"}

    if request.method == 'POST':
        post_data = request.get_json()

        Books.append({
            'id': ID.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            })
        
        response['message'] = 'Book added successfully'

    else:
        response['books'] = Books
    return jsonify(response)

#   Register the application routes
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

#app.add_url_rule('/', view_func=BookShelf().as_view('index.html'))


#   Run the program
if __name__ == '__main__':
    app.run()

