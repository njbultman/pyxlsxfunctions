import numpy as np

def SUMIF(sum_list, condition_list, condition):
    """Sum a list based on a specfic condition in another list.

    Parameters
    ----------
    sum_list : list or array
        list or array that will be summed. Length must match condition_list.
    condition_list : list or array
        list or array that will be checked against condition for summation. Length must match sum_list.
    condition : string
        string to be checked against condition list.

    Returns
    -------
    numeric or integer
        The total sum of numbers matching condition from condition list
    """
    if(len(sum_list) == len(condition_list)):
        if(type(condition) == str):
            sum_list = np.array(sum_list)
            condition_list = np.array(condition_list)
            return(sum(sum_list[condition_list == condition]))
        else:
            print('Invalid type: condition must be a string.')
    else:
        print('Length of sum_list and condition_list must match.')

def COUNTIF(count_list, condition_list, condition):
    """Count the instances in a list based on a specfic condition in another list.

    Parameters
    ----------
    count_list : list or array
        list or array that will be summed. Length must match condition_list.
    condition_list : list or array
        list or array that will be checked against condition for summation. Length must match sum_list.
    condition : string
        string to be checked against condition list.

    Returns
    -------
    numeric or integer
        The total count of instances matching condition from condition list
    """
    if(len(count_list) == len(condition_list)):
        if(type(condition) == str):
            count_list = np.array(count_list)
            condition_list = np.array(condition_list)
            return(len(count_list[condition_list == condition]))
        else:
            print('Invalid type: condition must be a string.')
    else:
        print('Length of sum_list and condition_list must match.')
        