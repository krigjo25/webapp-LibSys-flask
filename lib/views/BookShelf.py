#  Index view

#   Importing required dependencies
import uuid as ID

#   Importing  required dependencies
from dotenv import load_dotenv
from flask import jsonify, request
from flask.views import MethodView

#   Importing custom libraries
from lib.utility_tools.tools import UtilityTools

#   Loading environment variables
load_dotenv()

BOOKS = [
    {
        'id': ID.uuid4().hex,
        'title': 'The Alchemist',
        'author': 'Paulo Coelho',
    },
    {
        'id': ID.uuid4().hex,
        'title': 'The Secret',
        'author': 'Rhonda Byrne'
    }]

class BookMananger(MethodView):

    def __init__(self, books = BOOKS, *args, **kwargs):

        self.tool = UtilityTools()
        self.BOOKS = BOOKS
    
    def get(self):

        response = {}

        #   Ensure that the request method is GET
        if request.method == 'GET':

            response['books'] = self.BOOKS
            response['status'] = "success"
            response['message'] = "Books fetched successfully"

        else:
            response['status'] = "Unsuccessful"
            response['message'] = "An error Occured while attempting to process the request"
        
        return jsonify(response)
    
    def post(self):

        #   Initialize the json response
        response = {}

        #   Ensure that the request method is POST
        if request.method == 'POST':
            print("test")

            #  Fetch the requested data
            data = request.get_json()

            book = {
                'id': ID.uuid4().hex,
                'title': data['title'],
                'author': data['author']
            }

            self.BOOKS.append(book)

            response = {
                'status': "success", 
                'message': "Book added successfully"
                }
        else:
            response['status'] = "Unsuccessful"
            response['message'] = "An error Occured while attempting to process the request"
        
        return jsonify(response)
    
    def put(self, BID):

        response = {}
        #   Ensure that the request method is PUT (Update)
        if request.method == 'PUT':

            #   Initialize the response and fetch the request data
            response['status'] = "success"
            data = request.get_json()
            print(BID, data)


            #   Ensure that the book exists in the dictionary
            if self.tool.Check(self.BOOKS, BID):
                
                dictionary = {
                    'id': BID,
                    'title': data.get('title'),
                    'author': data.get('author')
                }

                #   Remove the old book from the dictionary
                self.tool.Purge(self.BOOKS, BID)

                #   Add the updated book to the dictionary
                self.BOOKS.append(dictionary)
                response['message'] = 'Book updated successfully'
            else:
                response['message'] = "Book does not exist"

        else:
            response['status'] = "Unsuccessful"
            response['message'] = "An error Occured while attempting to process the request"

        return jsonify(response)

    def delete(self, BID):

        response = {}

        #   Ensure that the request method is DELETE
        if request.method == 'DELETE':

            response['status'] = "success"
            response['message'] = "Book deleted successfully"
            response['books'] = self.tool.Purge(self.BOOKS, BID)

        return jsonify(response)