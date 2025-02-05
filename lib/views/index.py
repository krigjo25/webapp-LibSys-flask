#  Index view

#   Importing  required dependencies
from flask import jsonify, request
from flask.views import MethodView
from dotenv import load_dotenv

#   Loading environment variables
load_dotenv()

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

class BookShelf(MethodView):

    methods = ['GET', 'POST', 'PUT', 'DELETE']

    def get(self):

        json = {
            'status': "Success",
            'Message':"Book retrieved",
            'books':Books}

        return jsonify(json)
    
    def post(self):
        if request.method == 'POST':

            data = request.get_json()
            Books.append(
                {
                    'id': Books[-1]['id'] + 1,
                    'title': data['title'],
                    'author': data['author'],
                    'read': False
                 })
            
            response = {
                'status': "success", 
                'message': "Book added successfully",
                'books': Books}
            
            return jsonify(response)