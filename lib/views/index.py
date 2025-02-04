#  Index view

#   Importing  required dependencies
from flask import render_template
from flask.views import MethodView
from dotenv import load_dotenv

#   Loading environment variables
load_dotenv()

class Index(MethodView):

    methods = ['GET', 'POST', 'PUT', 'DELETE']

    def get(self):
        return render_template('index.html')