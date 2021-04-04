def UPPER(text):
    """Convert lengths between inches and feet.

    Parameters
    ----------
    x : array_like
        Lengths in feet.
    reverse : bool, optional
        If this is set to true this function converts from feet to inches
        instead of the default behaviour of inches to feet.

    Returns
    -------
    ndarray
        An array of converted lengths with the same shape as `x`. If `x` is a
        0-d array, then a scalar is returned.
    """
    return(text.upper())
    