#   Database tables for the app

from core_files import db
#   Importing the required modules

from sqlalchemy import Column, Integer, String, REAL

class Book(db.Model):
    """
        *   Books model class
        *   Initialize the class model
    """

    __tablename__ = "Books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    bookID = Column(String, unique=True)
    title = Column(String(100), nullable=False, unique=True)
    author = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    genre = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    img_path = Column(String(100), nullable=False)
    rating = Column(REAL, nullable=False)
    reviewers = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Book {__class__.__name__}"
    
    def ConvertToDict(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'genre': self.genre,
            'description': self.description,
            'path': self.img_path,
            'rating': self.rating,
            'reviews': self.reviewers
        }