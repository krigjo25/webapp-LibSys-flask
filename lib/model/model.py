#   Databases models for the app

#   Importing the required modules
from sqlalchemy import Column, Integer, String, REAL
from flask_sqlalchemy import SQLAlchemy

#   Initialize the database
db = SQLAlchemy()
session = db.session

class Books(db.Model):
    """
        *   Books model class
        *   Define the database schema
    """

    __tablename__ = "Books"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    genre = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    cover = Column(String(100), nullable=False)
    rating = Column(REAL, nullable=False)
    reviews = Column(String(100), nullable=False)

    def __repr__(self):
        return f""