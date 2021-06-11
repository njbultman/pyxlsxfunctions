import datetime as dt

def NOW():
    """Returns the current date and time in the local time zone.

    Returns
    -------
    string
        A datetime string with the current date and time in the local time zone.
    """
    return(str(dt.datetime.now()))

def TODAY():
    """Returns the current date.

    Returns
    -------
    string
        A date string with the current date (using local time zone).
    """
    return(str(dt.date.today()))
    