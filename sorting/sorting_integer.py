#!python
from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n+k) where n is the number of elements in input array and k is the range of input
    TODO: Memory usage: O(n+k)
    
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



def bucket_sort(numbers):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n + k) for best case and average case and O(n^2) for the worst case
    Memory usage: O(n + k)"""
    # FIXME: Improve this to mutate input instead of creating new output list

    # Find range of given numbers (minimum and maximum values)
    max_val = max(numbers)
    # use length of the list to determine which value in the list goes into which bucket
    size = max_val/len(numbers)

    # Create list of buckets to store numbers in subranges of input range
    buckets_list = [] 
    for x in range(len(numbers)):
      buckets_list.append([])

    # Loop over given numbers and place each item in appropriate bucket based on size 
    for i in range(len(numbers)):
      j = int(numbers[i] / size)
      if j != len (numbers):
          buckets_list[j].append(numbers[i])
    else:
        buckets_list[len(numbers) - 1].append(numbers[i])

    # Sort elements within the buckets using Insertion Sort
    for z in range(len(numbers)):
        insertion_sort(buckets_list[z])

    # Concatenate buckets with sorted elements into a single list
    # Loop over buckets and append each bucket's numbers into output list
    output_list = []
    for x in range(len(numbers)):
        output_list = output_list + buckets_list[x]
    return output_list