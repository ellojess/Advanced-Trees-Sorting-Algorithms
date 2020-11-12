#!python

from sorting_iterative import insertion_sort

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