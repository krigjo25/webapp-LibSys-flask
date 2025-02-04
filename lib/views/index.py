#  Index view

#   Importing  required dependencies
from flask import jsonify
from flask.views import MethodView
from dotenv import load_dotenv

#   Loading environment variables
load_dotenv()

class Index(MethodView):

    methods = ['GET', 'POST', 'PUT', 'DELETE']

    def ping_pong(self):
        return jsonify('Welcome to the application')