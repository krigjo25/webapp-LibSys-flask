#   Admin interface view
from flask_admin.contrib.sqla import ModelView

from lib.model.model import Books
class BooksView(ModelView):
    """
        *   Books view class
        *   Define the admin interface
    """
    column_list = ('title', 'author', 'year', 'genre', 'description', 'cover', 'rating', 'reviews')
    column_labels = dict(title='Title', author='Author', year='Year', genre='Genre', description='Description', cover='Cover', rating='Rating', reviews='Reviews')
    column_filters = ('title', 'author', 'year', 'genre')