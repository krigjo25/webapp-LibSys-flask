# Entry point for the application
import uuid as ID

# Importing the required libraries
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_session import Session
from flask_cors import CORS

#   Import application repositories
from lib.config.config import DevelopmentConfig
from lib.utility_tools.tools import UtilityTools
#   Import the application views
from lib.views.BookShelf import BookMananger

#   Load the environment variables from the .env file
load_dotenv()

#   Initialize the Flask application
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
Session(app)




Mananger = BookMananger()

#   Enable the CORS for the application
CORS(app, resources={r"/*": {"origins": '*'}})


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
    },
    {
        'id': ID.uuid4().hex,
        'title': 'The Secret',
        'author': 'Rhonda Byrne',
    }]

@app.route('/', methods=['GET'])
def FetchBooks():

    response = {}

    #   Ensure that the request method is GET
    if request.method == 'GET':
        response['status'] = "success"
        response['books'] = Books
        response['message'] = "Books fetched successfully"

    else:
        response['status'] = "Unsuccessful"
        response['message'] = "An error Occured while attempting to process the request"

    return jsonify(response)

@app.route('/', methods=['POST'])
def CreateBook():

    response = {}

    #   Ensure that the request method is POST
    if request.method == 'POST':

        #   Initialize the response and fetch the request data
        response['status'] = "success"
        data = request.get_json()

        #   Initialize the book and append it to the dictionary
        dictionary = {
            'id': ID.uuid4().hex,
            'title': data.get('title'),
            'author': data.get('author')}
        
        Books.append(dictionary)
        
        response['message'] = 'Book added successfully'

    else:
        response['status'] = "Unsuccessful"
        response['message'] = "An error Occured while attempting to process the request"

    return jsonify(response)

@app.route('/<BID>', methods=['PUT'])
def UpdateBook(BID):

    response = {}

    #   Ensure that the request method is PUT (Update)
    if request.method == 'PUT':

        #   Initialize the response and fetch the request data
        response['status'] = "success"
        data = request.get_json()
        print(BID,data)


        #   Ensure that the book exists in the dictionary
        if UtilityTools.Check(Books, BID):
            
            dictionary = {
                'id': BID,
                'title': data.get('title'),
                'author': data.get('author')
            }

            #   Remove the old book from the dictionary
            UtilityTools.Purge(Books, BID)

            #   Add the updated book to the dictionary
            Books.append(dictionary)
            response['message'] = 'Book updated successfully'
        else:
            response['message'] = "Book does not exist"

    else:
        response['status'] = "Unsuccessful"
        response['message'] = "An error Occured while attempting to process the request"

    return jsonify(response)

@app.route('/<BID>', methods=['DELETE'])
def DeleteBook(BID):
    
    response = {}

    #   Ensure that the request method is DELETE
    if request.method == 'DELETE':

        response['status'] = "success"

        #   Ensure that the book exists in the dictionary
        if UtilityTools.Check(Books, BID):

            #   Remove the book from the dictionary
            UtilityTools.Purge(Books, BID)

            response['message'] = "Book deleted successfully"
        else:
            response['message'] = "Book does not exist"

    response['status'] = "An error Occured while attempting to process the request"
    response['message'] = "A bad request were sent to the server"

    return jsonify(response)

#   Register the application routes
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


#   Run the program
if __name__ == '__main__':
    app.run()

