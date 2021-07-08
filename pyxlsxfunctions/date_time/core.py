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

def DAYS(date1, date2):
    """Given two strings of dates, calculate the difference in days between the two.

    Parameters
    ----------
    date1 : string
        start date in the form of a string: 'YYYY-MM-DD'
    date2 : string
        end date in the form of a string: 'YYYY-MM-DD'

    Returns
    -------
    int
        An integer with the difference between the start date and the end date.
    """
    if(type(date1) == str and type(date2) == str):
        if(len(date1.split('-')) == 3 and len(date2.split('-')) == 3):
            date1_split = date1.split('-')
            date1 = dt.date(int(date1_split[0]), int(date1_split[1]), int(date1_split[2]))
            date2_split = date2.split('-')
            date2 = dt.date(int(date2_split[0]), int(date2_split[1]), int(date2_split[2]))
            diff = date2 - date1
            return(diff.days)
        else:
            print('Invalid string: did you enter the dates in the proper YYYY-MM-DD format?')
    else:
        print('Invalid type: passed arguments other than strings.')

    