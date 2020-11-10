#!python

def raise_power(base, power):
    """
    a recursive function called raise_power() that takes in two integer parameters, 
    the first parameter being the base number and the second parameter being the power 
    you want to raise it to
    """

    if power == 0:
        return 1
    
    # multiply base by itself until power reaches 0
    if power >= 1:
        return base * raise_power(base, power - 1)

    