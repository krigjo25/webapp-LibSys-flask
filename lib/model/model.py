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
    id = Column(Integer, unique=True, autoincrement=True)
    bookID = Column(String, primary_key=True, nullable=False)
    title = Column(String(100), nullable=True, unique=True)
    author = Column(String(100), nullable=True)
    year = Column(Integer, nullable=True)
    genre = Column(String(100), nullable=True)
    description = Column(String(100), nullable=True)
    img_path = Column(String(100), nullable=True)
    rating = Column(REAL, nullable=True)
    reviewers = Column(String(100), nullable=True)

    def __repr__(self):
        return f"<Book title : {self.title} Book id : {self.bookID} row : {self.id}>"
    
    def ConvertToDict(self):
        return {
            'id': self.bookID,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'genre': self.genre,
            'description': self.description,
            'path': self.img_path,
            'reviews': [{'name':self.reviewers,
                        'rating': self.rating}]
        }