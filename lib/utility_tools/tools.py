

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

def Purge(arg:dict, ID:str):
    """
        *  Delete the book from the dictionary

        param: BID
        return: None
    """
    for element in arg:

        #   Ensure that the element exists in the dictionary
        if element['id'] == ID:

            #   Remove the element from the dictionary
            arg.remove(element)

            return arg