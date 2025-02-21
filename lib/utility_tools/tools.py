#   Utility tools for the application

#   Import the necessary dependencies
import os, uuid as ID

#   Importing custom dependencies
from lib.config.logger import UtilityWatcher

class UtilityTools(object):

    def __init__(self):

        #   Initializing the logger
        self.log = UtilityWatcher()
        self.log.FileHandler()


    def Check(self, Books:list, BID:str):
    
        """
            *  Ensure that the element exists in the dictionary

            param: ID, Argument
            param: ID
            return: True or False
        """
            
        for book in Books:

            #   Ensure that the element exists in the dictionary
            if book['id'] == BID:
                self.log.info(f"Book with ID: {BID} exists in the dictionary.")
                return True

            self.log.warn(f"Book with ID: {BID} does not exist in the dictionary.")
        return False

    def Purge(self, arg:list, ID:str):
        """
            *  Delete the book from the dictionary

            param: BID
            return: None
        """

        #   Ensure that the element exists in the dictionary
        if self.Check(arg, ID):
            for i in arg:

                #   Ensure that the element exists in the dictionary
                if i['id'] == ID:

                    #   Remove the element from the dictionary
                    arg.remove(i)
            self.log.info(f"Book with ID: {ID} has been removed from the dictionary.")

        return arg
    
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