#  Book's endpoint

#   Importing required dependencies
import uuid as ID

#   Importing  required dependencies
from core_files import app
from dotenv import load_dotenv
from flask.views import MethodView
from flask import jsonify, request

#   Importing custom libraries
from lib.model.model import Book
from lib.config.logger import MethodWatcher
from lib.utility_tools.tools import UtilityTools

#   Loading environment variables
load_dotenv()

logger = MethodWatcher()
logger.FileHandler()

class BookMananger(MethodView):

    def __init__(self, *args, **kwargs):

        #   Initialize the logger
        self.orgins = '*'
        with app.app_context():
            books = Book().query.all()
        self.BOOKS = [book.ConvertToDict() for book in books]
        self.logger = logger
        self.tool = UtilityTools(self.BOOKS)
        
    
    def get(self):

        response = {}

        #   Ensure that the request method is GET
        if request.method == 'GET':
            
            self.tool.FetchImages()

            response['code'] = 200
            response['status'] = "success"
            response['books'] = self.BOOKS

            self.logger.info(f"Status : {response['code']}\nMethod : {request.method}\nBooks: {response['books']}")
        else:
            response['status'] = "Unsuccessful"
            response['message'] = "An error Occured while attempting to process the request"

            self.logger.error(f"Headers : {request.headers}\n Error : {response['message']} \n Status : {response['status']} Method : {request.method}")
        
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
                'author': [i for i in data['author']]
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
            if self.tool.Purge(BID):
            
                dictionary = {
                    'id': BID,
                    'title': data['title'],
                    'author': str(data['author']).split(',')
                }

                #   Add the new book to the dictionary
                self.BOOKS.append(dictionary)
                response['message'] = "Book updated successfully"
                self.logger.info(f"Method :{request.method}\nData :{dictionary} ")
            else:
                response['message'] = "Book does not exist"
                self.logger.error(f"Headers : {request.headers}\n Error : {response['message']} \n book.id : {BID} Method : {request.method}")
            

        else:
            response['status'] = "Unsuccessful"
            response['message'] = "An error Occured while attempting to process the request"
            self.logger.error(f"Status : {response['code']} Method : {request.method} Headers : {request.headers}")

        return jsonify(response)

    def delete(self, BID):

        response = {}
        
        #   Ensure that the request method is DELETE
        if request.method == 'DELETE' and BID is not None:
            print(BID)
            response['status'] = "success"
            response['message'] = self.tool.Purge(BID)
            response['books'] = self.BOOKS
            


        return jsonify(response)
