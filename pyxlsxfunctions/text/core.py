def UPPER(text):
    """Convert all text to uppercase.

    Parameters
    ----------
    text : list or string
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
    text : list or string
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

def LEFT(text, n):
    """Slices string(s) a specified number of characters from left.

    Parameters
    ----------
    text : list or string
        String(s) to be sliced from left.
    n : integer
        Number of characters to slice from left. Must be greater than zero.

    Returns
    -------
    list or string
        A list of converted strings or converted string that were sliced n characters from left.
    """
    if n > 0:
        if type(text) == str:
            return(text[0:n])
        elif type(text) == list:
            try:
                text_return = [i[0:n] for i in text]
                return(text_return)
            except:
                print('Invalid list: please enter a list of strings.')
        else:
            print('Invalid type: please enter a string or list of strings.')
    else:
        print('n must be greater than zero.')

def RIGHT(text, n):
    """Slices string(s) a specified number of characters from right.

    Parameters
    ----------
    text : list or string
        String(s) to be sliced from right.
    n : integer
        Number of characters to slice from right. Must be greater than zero.

    Returns
    -------
    list or string
        A list of converted strings or converted string that were sliced n characters from right.
    """
    if n > 0:
        if type(text) == str:
            return(text[-n:])
        elif type(text) == list:
            try:
                text_return = [i[-n:] for i in text]
                return(text_return)
            except:
                print('Invalid list: please enter a list of strings.')
        else:
            print('Invalid type: please enter a string or list of strings.')
    else:
        print('n must be greater than zero.')
    