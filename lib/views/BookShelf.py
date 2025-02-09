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
        'inf':[{
            'description' :'The Alchemist is a novel by Brazilian author Paulo Coelho that was first published in 1988. Originally written in Portuguese, it became an international bestseller translated into some 70 languages as of 2016. An allegorical novel, The Alchemist follows a young Andalusian shepherd in his journey to the pyramids of Egypt, after having a recurring dream of finding a treasure there.',
            'genre': 'Adventure, Quest, Drama, Fantasy, Fiction, Philosophical fiction',
            'rating': 4.5,
            'year': 1988
            }],
        'img':''
    },
    {
        'id': ID.uuid4().hex,
        'title': 'The Secret',
        'author': 'Rhonda Byrne',
        'info':[{
            'description':'The Secret is a best-selling 2006 self-help book by Rhonda Byrne, based on the earlier film of the same name. It is based on the belief of the law of attraction, which claims that thoughts can change a person\'s life directly. The book has sold 30 million copies worldwide and has been translated into 50 languages.',
            'genre': 'Self-help book, Personal development',
            'rating': 4.2,
            'year': 2006 
        }],
        'img':''

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
                'message': "Book added successfully",
                'books': self.BOOKS
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

            #   Ensure that the book exists in the dictionary
            if self.tool.Purge(self.BOOKS, BID):
                
                dictionary = {
                    'id': BID,
                    'title': data.get('title'),
                    'author': data.get('author')
                }

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