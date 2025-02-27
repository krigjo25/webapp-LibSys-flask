#   Utility tools for the application

#   Import the necessary dependencies
import os, uuid as ID

#   Importing custom dependencies
from lib.config.logger import UtilityWatcher
from core_files import app, db
class UtilityTools(object):

    def __init__(self, books):

        #   Initializing the logger
        self.log = UtilityWatcher()
        self.log.FileHandler()
        self.books = books


    def Check(self, BID:str):
    
        """
            *  Ensure that the element exists in the dictionary

            param: ID, Argument
            param: ID
            return: True or False
        """
            
        for book in self.books:

            #   Ensure that the element exists in the dictionary
            if book['id'] == BID:
                self.log.info(f"Book with ID: {BID} exists in the dictionary.")
                return True

            self.log.warn(f"Book with ID: {BID} does not exist in the dictionary.")
        return False

    def Purge(self, ID:str):
        """
            *  Delete the book from the dictionary

            param: BID
            return: None
        """

        #   Ensure that the element exists in the dictionary
        if self.Check(ID):
            for i in self.books:

                #   Ensure that the element exists in the dictionary
                if i['bookID'] == ID:
                    
                    with app.app_context():
                        db.session.delete(i)
                        db.session.commit()
                    return "Book Deleted Successfully"

        return "Book does not exist in the dictionary"

    def FetchImages(self):
        """
            *  Fetch the images from the directory

            param: None
            return: list
        """

        #   Initialize the path to the images
        PATH = "VueClient/src/assets/img/"
        for i in os.listdir(PATH):
            print(i)
        return