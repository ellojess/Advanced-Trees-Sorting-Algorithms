#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list

    new_sorted_list = [] 

    # if both lists are empty 
    if not items1 and not items2:
      return new_sorted_list
    # if items1 is not empty but item2 is empty
    if items1 and not items2: 
      return new_sorted_list + items1
    # if items2 is not empty but item1 is empty
    if not items1 and items2: 
      return new_sorted_list + items2
    # if neither lists are empty
    if items1 and items2: 
      # if item in item1 is less than or equal to item in items2
      if items1[0] <= items2[0]:
        # append item in item1 to new_sorted_list
        new_sorted_list.append(items1[0])
        new_sorted_list += merge(items1[1:], items2) # recursive call until end of list
        print(new_sorted_list)
      # if item in item1 is greater than item in items2
      if items1[0] > items2[0]:
        # append item in item2 to new_sorted_list
        new_sorted_list.append(items2[0])
        new_sorted_list += merge(items1, items2[1:]) # recursive call until end of list
    return new_sorted_list



def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # if list is empty 
    if not items or len(items) <= 1:
      return items

    # TODO: Split items list into approximately equal halves
    mid = len(items)//2
    left = items[0:mid]
    right = items[mid:]
    # Sort each half using any other sorting algorithm
    # Merge sorted halves into one list in sorted order
    return merge(split_sort_merge(left), split_sort_merge(right))



def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # Check if list is empty or so small it's already sorted (base case)
    if not items or len(items) <= 1:
      return items

    # Split items list into approximately equal halves
    mid = len(items)//2
    left = items[0:mid]
    right = items[mid:]
    # Sort each half using any other sorting algorithm
    # Merge sorted halves into one list in sorted order
    return merge(merge_sort(left), merge_sort(right))


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p

    


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

