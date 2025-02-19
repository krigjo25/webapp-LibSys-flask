#  Index view

#   Importing required dependencies
import os, uuid as ID

#   Importing  required dependencies
from dotenv import load_dotenv
from flask import jsonify, request, make_response
from flask.views import MethodView

#   Importing custom libraries
from lib.utility_tools.tools import UtilityTools
from lib.config.logger import MethodWatcher

#   Loading environment variables
load_dotenv()

BOOKS = [
    {
        'img':[''],
        'selected': False,
        'published': 1988,
        'id': ID.uuid4().hex,
        'title': "The Alchemist",
        'author': ['Paulo Coelho'],
        'publisher': "HarperCollins Publishers",
        'genre': ['Adventure', 'Quest', 'Drama', 'Fantasy', 'Fiction', 'Philosophical fiction'],
        'description' :'The Alchemist is a novel by Brazilian author Paulo Coelho that was first published in 1988. Originally written in Portuguese, it became an international bestseller translated into some 70 languages as of 2016. An allegorical novel, The Alchemist follows a young Andalusian shepherd in his journey to the pyramids of Egypt, after having a recurring dream of finding a treasure there.',

        'rating': [
            {
                'Books.com':4.5
            }],
    },
    {
        'img':[''],
        'published': 2006,
        'selected': False,
        'id': ID.uuid4().hex,
        'title': "The Secret",
        'author': ['Rhonda Byrne'],
        'publisher': "Atria Books Pty Ltd",
        'genre': ['Self-help book', 'Personal development'],
        'description':'The Secret is a best-selling 2006 self-help book by Rhonda Byrne, based on the earlier film of the same name. It is based on the belief of the law of attraction, which claims that thoughts can change a person\'s life directly. The book has sold 30 million copies worldwide and has been translated into 50 languages.',

        'rating': [
            {
                'Books.com':4.2
            }],
    }]

logger = MethodWatcher()
logger.FileHandler()

class BookMananger(MethodView):

    def __init__(self, books = BOOKS, *args, **kwargs):

        #   Initialize the logger
        self.logger = logger
        

        self.tool = UtilityTools()
        self.BOOKS = BOOKS

        self.orgins = '*'
    
    def get(self):

        response = {}

        #   Ensure that the request method is GET
        if request.method == 'GET':

            response['code'] = 200
            response['status'] = "success"
            response['books'] = self.BOOKS

            self.logger.info(f"Status : {response['code']}")

        else:
            response['status'] = "Unsuccessful"
            response['message'] = "An error Occured while attempting to process the request"

            self.logger.error(f"Headers : {request.headers}\n Error : {response['message']} \n Status : {response['status']}")
        
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
                'books': self.BOOKS,
                'code': 201,
                'message': "Book added successfully",
                }

            self.logger.info(f"Status : {response['code']}")

        else:
            response['status'] = "Unsuccessful"
            response['code'] = 400
            response['message'] = "An error Occured while attempting to process the request"

            self.logger.error(f"Status : {response['code']} Method : {request.method} Headers : {request.headers}")
        
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
                    'title': data['title'],
                    'author': data['author']
                }

                #   Add the updated book to the dictionary
                self.BOOKS.append(dictionary)
                response['message'] = "Book updated successfully"

                self.logger.info(f"Status : {response['code']}")
            else:
                response['message'] = "Book does not exist"
                self.logger.error(f"Bookd id : {BID} does not exist")

        else:
            response['status'] = "Unsuccessful"
            response['message'] = "An error Occured while attempting to process the request"
            self.logger.error(f"Status : {response['code']} Method : {request.method} Headers : {request.headers}")

        return jsonify(response)

    def delete(self, BID):

        response = {}

        #   Ensure that the request method is DELETE
        if request.method == 'DELETE':

            response['status'] = "success"
            response['message'] = "Book deleted successfully"
            response['books'] = self.tool.Purge(self.BOOKS, BID)


        return jsonify(response)