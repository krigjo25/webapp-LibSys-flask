# Entry point for the application

# Importing the required libraries
from core_files import app, db, admin, logger

#   Import application repositories
from lib.model.model import Book
from lib.admin.views import BooksView
from lib.views.BookShelf import BookMananger
from lib.model.preload import alchemist, secrets

#   Endpoints
Mananger = BookMananger()
app.add_url_rule('/', view_func=Mananger.as_view('get', methods=['GET', 'POST']))
app.add_url_rule('/<BID>', view_func=Mananger.as_view('update', methods=['PUT', 'DELETE']))    

#   Add the model to the admin interface
admin.add_view(BooksView(Book, db.session))
#   Log the application configurations

for key, value in app.config.items():
    logger.warn(f"{key} : {value}")

logger.info('Application Configurations END')

#   Disable the cache
@app.after_request
def after_request(response):
    response.headers['Expires'] = 0
    response.headers['Pragma'] = "no-cache"
    response.headers['Cache-Control'] = "no-cache, no-store, must-revalidate"
    return response

with app.app_context():
    db.create_all()
    #db.session.add(alchemist)
    #db.session.add(secrets)
    db.session.commit()

#   Run the program
if __name__ == '__main__':
    app.run()