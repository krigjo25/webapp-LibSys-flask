#  Book's endpoint

#   Importing required dependencies
import uuid as ID

#   Importing  required dependencies
from core_files import app, db
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
            self.books = Book().query.all()

        self.logger = logger
        self.tool = UtilityTools()
        self.BOOKS = [book.ConvertToDict() for book in self.books]

    def get(self):

        response = {}

        #   Ensure that the request method is GET
        if request.method == 'GET':

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

        #   Ensure that the request method is POST
        if request.method == 'POST':

            #  Fetch the requested data
            data = request.get_json()

            #   Log the data which is retrieved
            self.logger.warn(f"Data retrieved")
            for key, value in data.items():
                self.logger.info(f"{key} : {value}")
            self.logger.warn(f"END OF LIST")

            #   Initialize a new book object
            book = Book(title = data['title'], genre = data['genre'],
                        img_path = data['image'], year = data['year'],
                        author = data['author'], bookID = ID.uuid4().hex,
                        rating = data['review']['rating'], description = data['description'])
    
            with app.app_context():
                db.session.add(book)
                db.session.commit()

            response = self.response(200)

        else:
            response = self.response(405)

        return response
    
    def put(self, BID):

        #   Ensure that the request method is PUT (Update)
        if request.method == 'PUT':

            #   fetch the current book
            book = Book().query.get(BID)
            #   Initialize the response and fetch the request data
            
            data = request.get_json()

            #   Update the book object
            for key, value in data.items():

                #   Ensure the integerty for the value, and book
                if value is not None and hasattr(book, key) and key != 'id':
                    setattr(book, key, value)

                db.session.commit()
            
            #   Success response
            response = self.response(200, book = book.ConvertToDict())
            self.logger.info(f"Data retrieved: {data} ")

        else:
            response = self.response(405)
            self.logger.error(f"Status : {response['code']} Method : {request.method} Headers : {request.headers}")

        return response

    def delete(self, BID):
        
        #   Ensure that the request method is DELETE
        if request.method == 'DELETE' and BID is not None:
            
            if self.tool.Purge(BID):
                
                response = self.response(200, BID)
            else:
               
               response = self.response(404)

        else:
            response = self.response(405)

        return response

    def response(self, status:int = 200, message:str = None, BID:str = None, book:dict = None):

        response = {}
        match status:

            case 200:
                response['books'] = self.BOOKS
                response['status'] = status

                if not message:
                    response['message'] = "The operation was sucssessfull !"
    
                if book:
                    response['books'] = [i for i in book]
            case 404:
                response['status'] = status
                if not message:
                    response['message'] = "Checked everywhere, the book was not found."

                self.logger.error(f"  Method : {request.method} | Book ID : {BID}")

            case 405:
                response['status'] = status
                if not message:

                    response['message'] = "Something smells fishy, ensure the request method is correct."
                
                self.logger.warn(f"Headers : {request.headers}\n  Method : {request.method} | Book ID : {BID}")



        return jsonify({'status': status, 'message': message})