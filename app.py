# Entry point for the application

# Importing the required libraries
from flask import Flask
from dotenv import load_dotenv
from flask_session import Session
from flask_core import CORS


#   Import application repositories
from lib.views import views
from lib.config.config import DevelopmentConfig


#   Load the environment variables from the .env file
load_dotenv()

app = Flask(__name__)

#   Load the configuration settings for the app
app.config.from_object(DevelopmentConfig)
Session(app)

#   Enable the CORS policy
CORS(app, resources={r"/*": {"origins": "*"}})


#   Application webworkers

#   Register the application routes
app.add_url_rule('/', view_func=Index().as_view('index.html'))


#   Run the program
if __name__ == '__main__':
    app.run()

