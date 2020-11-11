#!python

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?
    
    numbers => input array 
    position => temporary array 
    result => sorted array 
    """
    # Find range of given numbers (minimum and maximum integer values)
    # Create list of counts with a slot for each number in input range
    # Loop over given numbers and increment each number's count
    # Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    n = len(numbers)
    k = max(numbers) + 1 

    # initialize position list 
    position = [0] * k 

    # Create list of counts with a slot for each number in input range
    # increment index val by 1 
    for val in numbers: 
      position[val] += 1 

    # determine number of items in list are greater than val, update corresponding index 
    s = 0 
    for i in range(0, k): 
      temp = position[i]
      position[i] = s 
      s += temp 

    # initialize result list by None 
    result = [None] * n 

    # place items directly into sorted position in result list based on info from position list 
    for val in numbers: 
      result[position[val]] = val
      position[val] += 1 

    return result 