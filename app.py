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


"""Books = [
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


#   Register the application routes
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')
"""
app.add_url_rule('/', view_func=Mananger.as_view('get', methods=['GET']))
app.add_url_rule('/add', view_func=Mananger.as_view('post', methods=['POST']))
app.add_url_rule('/<BID>', view_func=Mananger.as_view('update', methods=['GET','PUT', 'DELETE']))    

#   Run the program
if __name__ == '__main__':
    app.run()

