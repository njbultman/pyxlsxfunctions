import datetime as dt
import pandas as pd

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

def EOMONTH(date, months):
    """Given a date string and the number of months in future, calculate the end of month for that date.

    Parameters
    ----------
    date : string
        start date in the form of a string: 'YYYY-MM-DD' or list of strings in same format
    months : int
        integer with how many months you want in future or past

    Returns
    -------
    string or list
        String or list of strings containing the end of the month corresponding to the months in future selected.
    """
    if(type(date) == str):
        try:
            date1 = pd.to_datetime(date)
            if months >= 1:
                date_final = date1 + pd.tseries.offsets.MonthEnd(months + 1)
            else:
                date_final = date1 + pd.tseries.offsets.MonthEnd(months)
            return(str(date_final)[0:10])
        except:
            print('Invalid string: please pass a valid date string.')
    elif(type(date) == list):
        try:
            date1 = pd.to_datetime(date)
            if months >= 1:
                date_final = date1 + pd.tseries.offsets.MonthEnd(months + 1)
            else:
                date_final = date1 + pd.tseries.offsets.MonthEnd(months)
            date_list_final = [str(i)[0:10] for i in date_final]
            return(date_list_final)
        except:
            print('Invalid list: pass a valid list of strings that can be converted to a date.')
    else:
        print('Invalid type: passed argument other than string or list into date.')

    