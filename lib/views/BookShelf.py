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

    }
]

class BookMananger(MethodView):

    def __init__(self):
        self.tool = UtilityTools()
        self.data = request.get_json()
        self.GET = request.method == 'GET'
        self.POST = request.method == 'POST'
        self.PUT = request.method == 'PUT'
        self.DELETE = request.method == 'DELETE'
    
    methods = ['GET', 'POST', 'PUT', 'DELETE']
    data = request.get_json()
    def FetchBooks(self):

        response = {}

        #   Ensure that the request method is GET
        if self.GET:

            response['books'] = Books
            response['status'] = "success"
            response['message'] = "Books fetched successfully"

        else:
            response['status'] = "Unsuccessful"
            response['message'] = "An error Occured while attempting to process the request"
        
        return jsonify(response)
    
    def CreateBook(self):

        #   Initialize the json response
        response = {}

        #   Ensure that the request method is POST
        if self.POST:

            #  Fetch the requested data
            data = request.get_json()

            book = {
                'id': ID.uuid4().hex,
                'title': data.get('title'),
                'author': data.get('author')
            }
            Books.append(book)
            
            response = {
                'status': "success", 
                'message': "Book added successfully",
                'books': Books}
        else:
            response['status'] = "Unsuccessful"
            response['message'] = "An error Occured while attempting to process the request"
        
        return jsonify(response)
    
    def UpdateBook(self, BID):

        response = {}
        #   Ensure that the request method is PUT (Update)
        if request.method == 'PUT':

            #   Initialize the response and fetch the request data
            response['status'] = "success"
            data = request.get_json()
            print(BID, data)


            #   Ensure that the book exists in the dictionary
            if self.tool.Check(Books, BID):
                
                dictionary = {
                    'id': BID,
                    'title': data.get('title'),
                    'author': data.get('author')
                }

                #   Remove the old book from the dictionary
                self.tool.Purge(Books, BID)

                #   Add the updated book to the dictionary
                Books.append(dictionary)
                response['message'] = 'Book updated successfully'
            else:
                response['message'] = "Book does not exist"

        else:
            response['status'] = "Unsuccessful"
            response['message'] = "An error Occured while attempting to process the request"

        return jsonify(response)

    def DeleteBook(self, BID):

        response = {}

        #   Ensure that the request method is DELETE
        if request.method == 'DELETE':

            response['status'] = "success"

            #   Ensure that the book exists in the dictionary
            if self.tool.Check(Books, BID):

                #   Remove the book from the dictionary
                self.tool.Purge(Books, BID)

                response['message'] = "Book deleted successfully"
            else:
                response['message'] = "Book does not exist"

        response['status'] = "An error Occured while attempting to process the request"
        response['message'] = "A bad request were sent to the server"

        return jsonify(response)