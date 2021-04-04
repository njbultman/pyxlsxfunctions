import datetime as dt

def NOW():
    """Returns the current date and time in the local time zone.

    Returns
    -------
    string
        A datetime string with the current date and time in the local time zone.
    """
    return(str(dt.datetime.now()))
    