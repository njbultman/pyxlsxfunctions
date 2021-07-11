import numpy as np

def UPPER(text):
    """Convert all text to uppercase.

    Parameters
    ----------
    text : list or string
        string(s) to be converted to uppercase.

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
        string(s) to be converted to lowercase.

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
        string(s) to be sliced from left.
    n : integer
        number of characters to slice from left. Must be greater than zero.

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
        string(s) to be sliced from right.
    n : integer
        number of characters to slice from right. Must be greater than zero.

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

def TRIM(text):
    """Strips leading/trailing whitespace from string(s).

    Parameters
    ----------
    text : list or string
        string(s) to have whitespace trimmed

    Returns
    -------
    list or string
        A list of trimmed strings or trimmed string with whitespace removed.
    """
    if type(text) == str:
        return(text.strip())
    elif type(text) == list:
        try:
            text_return = [i.strip() for i in text]
            return(text_return)
        except:
            print('Invalid list: please enter a list of strings.')
    else:
        print('Invalid type: please enter a string or list of strings.')

def FIND(char, text):
    """Finds the location of the character specified in the string or list of strings.

    Parameters
    ----------
    char : string
        one character string that you would like the location found in text
    text : list or string
        string(s) to have char found in

    Returns
    -------
    list or int
        A list of integers or an integer where the character specified was found.
    """
    if type(char) == str:
        if len(char) == 1:
            if type(text) == str:
                for i in range(len(text)):
                    if text[i] == char:
                        return(i)
                    else:
                        return(np.nan)
            elif type(text) == list:
                return_list = []
                try:
                    for i in text:
                        for z in range(len(i)):
                            if i[z] == char:
                                return_list.append(z)
                            elif i[z] != char and z == len(i) - 1 and (len(return_list) - 1) != text.index(i):
                                return_list.append(np.nan)
                    return(return_list)             
                except:
                    print('Invalid list: please enter a list of strings.')
            else:
                print('Invalid type: please enter a string or list of strings.')
        else:
            print('Invalid char length: char must be a one character string.')
    else:
        print('Invalid type: char must be a string.')
    