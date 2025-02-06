
import uuid as ID

class UtilityTools(object):


    def Check(Books:dict, BID:str):
    
        """
            *  Ensure that the element exists in the dictionary

            param: ID, Argument
            param: ID
            return: True or False
        """
            
        for book in Books:

            #   Ensure that the element exists in the dictionary
            if book['id'] == BID:

                return True
        return False

    def Purge(arg:list, ID:str):
        """
            *  Delete the book from the dictionary

            param: BID
            return: None
        """

        for i in arg:

            #   Ensure that the element exists in the dictionary
            if i['id'] == ID:

                #   Remove the element from the dictionary
                arg.remove(i)

        return arg
    
        """
            *  Initialize the book dictionary

            param: data
            return: dictionary
        """

        book = [
            {
            'id': ID.uuid4().hex,
            'title': 'The Alchemist',
            'author': 'Paulo Coelho',
            },
            {
                'id': ID.uuid4().hex,
                'title': 'The Secret',
                'author': 'Rhonda Byrne',

            }]
        return book