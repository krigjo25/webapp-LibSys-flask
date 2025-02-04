# Entry point for the application

# Importing the required libraries
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_session import Session
from flask_cors import CORS


#   Import application repositories
from lib.views.index import Index
from lib.config.config import DevelopmentConfig

#   Import the application views
from lib.views.index import Index

#   Load the environment variables from the .env file
load_dotenv()

app = Flask(__name__)

#   Load the configuration settings for the app
app.config.from_object(DevelopmentConfig)
Session(app)

#   Enable the CORS policy
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
        'id': 1,
        'title': 'The Alchemist',
        'author': 'Paulo Coelho',
        'read': True
    },
    {
        'id': 2,
        'title': 'The Secret',
        'author': 'Rhonda Byrne',
        'read': False
    }
]
@app.route('/', methods=['GET'])
def get_books():
    return jsonify({
        "status": "success",
        'books': Books})

#   Register the application routes
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

#app.add_url_rule('/', view_func=Index().as_view('index.html'))


#   Run the program
if __name__ == '__main__':
    app.run()

