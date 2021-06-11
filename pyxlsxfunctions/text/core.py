def UPPER(text):
    """Convert all text to uppercase.

    Parameters
    ----------
    x : list or string
        String(s) to be converted to uppercase.

    Returns
    -------
    list or string
        A list of converted strings or converted string to uppercase.
    """
    if type(text) == str:
        return((text).upper())
    elif type(text) == list:
        try:
            text_return = [(i).upper() for i in text]
            return(text_return)
        except:
            print('Invalid list: please enter a list of strings.')
    else:
        print('Invalid type: please enter a string or list of strings.')
        
        

def LOWER(text):
    """Convert all text to uppercase.

    Parameters
    ----------
    x : list or string
        String(s) to be converted to lowercase.

    Returns
    -------
    list or string
        A list of converted strings or converted string to lowercase.
    """
    if type(text) == str:
        return((text).lower())
    elif type(text) == list:
        try:
            text_return = [(i).lower() for i in text]
            return(text_return)
        except:
            print('Invalid list: please enter a list of strings.')
    else:
        print('Invalid type: please enter a string or list of strings.')
    