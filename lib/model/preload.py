from .model import Book
from uuid import uuid4
alchemist = Book(
    
    year = 1988,
    rating = 4.5,
    bookID = uuid4().hex,
    title = "The Alchemist",
    author = "Paulo Coelho",
    reviewers = "Books.com",
    img_path = "./src/assets/img/the_alchemist.jpeg",
    genre = "Adventure, Quest, Drama, Fantasy, Fiction, Philosophical fiction",
    description = "The Alchemist is a novel by Brazilian author Paulo Coelho that was first published in 1988. Originally written in Portuguese, it became an international bestseller translated into some 70 languages as of 2016. An allegorical novel, The Alchemist follows a young Andalusian shepherd in his journey to the pyramids of Egypt, after having a recurring dream of finding a treasure there.",
)

secrets = Book(
    
    year = 2006,
    rating = 4.2,
    bookID = uuid4().hex,
    title = "The Secret",
    reviewers = "Books.com",
    author = "Rhonda Byrne",
    description = "The Secret is a best",
    img_path = "./src/assets/img/the_secret.jpeg",
    genre = "Self-help book, Personal development",
)