# Entry point for the application
import os

# Importing the required libraries
from flask import Flask
from flask_cors import CORS
from flask_admin import Admin
from dotenv import load_dotenv
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView

#   Import application repositories

from lib.model.model import Books
from lib.admin.views import BooksView
from lib.config.logger import AppWatcher
from lib.views.BookShelf import BookMananger
from lib.config.config import DevelopmentConfig


#   Load the environment variables from the .env file
load_dotenv()

#   Initialize logger configurations
logger = AppWatcher()
logger.FileHandler()

#   Initialize the Flask application
app = Flask(__name__)

app.config.from_object(DevelopmentConfig)


#   Application configurations
#   Disable the cache
@app.after_request
def after_request(response):
    response.headers['Expires'] = 0
    response.headers['Pragma'] = "no-cache"
    response.headers['Cache-Control'] = "no-cache, no-store, must-revalidate"
    return response

#   Initialize the Admin interface
admin = Admin(app, name = 'BookShelf CRUD', template_mode = 'bootstrap3')

db = SQLAlchemy(app)
admin.add_view(BooksView(Books, db.session))

#   Initialize the session
Session(app)

#   CORS Configurations
CORS_ORIGINS = os.getenv('Local_ORIGINS') if app.config['DEBUG'] else os.getenv('CORS_ORIGINS')
CORS(app, resources={r"/.*": {"origins": {CORS_ORIGINS}}})

#   Endpoints
Mananger = BookMananger()
app.add_url_rule('/', view_func=Mananger.as_view('get', methods=['GET', 'POST']))
app.add_url_rule('/<BID>', view_func=Mananger.as_view('update', methods=['PUT', 'DELETE']))    

#   Log the application configurations
logger.info('Application Configurations START')
for key, value in app.config.items():
    logger.warn(f"{key} : {value}")

logger.info('Application Configurations END')


#   Run the program
if __name__ == '__main__':
    db.create_all()
    app.run()

