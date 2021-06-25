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

def AND(condition_1, condition_2):
    """Evaluates both conditions and returns True or False depending on how both conditions are evaluated.

    Parameters
    ----------
    condition_1 : condition that evaluates to True or False
        condition that will return True or False 
    condition_2 : condition that evaluates to True or False
        condition that will return True or False 

    Returns
    -------
    boolean
        True if both conditions are True, False otherwise
    """
    if(type(condition_1) == bool):
        if(type(condition_2) == bool):
            return(condition_1 and condition_2)
        else:
            print('Invalid type: second condition does not evaluate to True or False.')
    else:
        print('Invalid type: first condition does not evaluate to True or False.')
    
def OR(condition_1, condition_2):
    """Evaluates both conditions and returns True or False depending on how both conditions are evaluated.

    Parameters
    ----------
    condition_1 : condition that evaluates to True or False
        condition that will return True or False 
    condition_2 : condition that evaluates to True or False
        condition that will return True or False 

    Returns
    -------
    boolean
        True if one or both conditions are True, False otherwise
    """
    if(type(condition_1) == bool):
        if(type(condition_2) == bool):
            return(condition_1 or condition_2)
        else:
            print('Invalid type: second condition does not evaluate to True or False.')
    else:
        print('Invalid type: first condition does not evaluate to True or False.')

def IF(logical_statement, expression_true, expression_false):
    """Evaluates the logical statement. If it is true, reuturns the true expression. If not, returns false expression.

    Parameters
    ----------
    logical_statement : condition that evaluates to True or False
        condition that will return True or False 
    expression_true : expression
        expression that will be returned if logical statement is true
    expression_false : expression
        expression that will be returned if logical statement is false

    Returns
    -------
    expression
        True expression if logical statement is true, false expression otherwise
    """
    if(type(logical_statement) == bool):
        if(logical_statement == True):
            return(expression_true)
        else:
            return(expression_false)
    else:
        print('Invalid type: logical statement does not evaluate to True or False.')
        