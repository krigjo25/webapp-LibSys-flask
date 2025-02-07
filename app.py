# Entry point for the application
import uuid as ID

# Importing the required libraries
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_session import Session

#   Import application repositories
from lib.views.BookShelf import BookMananger
from lib.config.config import DevelopmentConfig

#   Load the environment variables from the .env file
load_dotenv()

#   Initialize the Flask application
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
Session(app)

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

Mananger = BookMananger()

app.add_url_rule('/', view_func=Mananger.as_view('get', methods=['GET', 'POST']))
app.add_url_rule('/<BID>', view_func=Mananger.as_view('update', methods=['GET','PUT', 'DELETE']))    

#   Run the program
if __name__ == '__main__':
    app.run()

