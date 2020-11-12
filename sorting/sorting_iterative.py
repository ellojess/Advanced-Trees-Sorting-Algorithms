#!python

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) 
    Memory usage: O(1) 
    
    Check that all adjacent items are in order, return early if so"""

    # loop through items in the list 
    for i in range(len(items)-1):
        current_item = items[i]
        next_item = items[i+1]
        # if next_item is less than current then exit loop and return False 
        if next_item <= current_item:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n)
    Memory usage: O(1)

    Repeat until all items are in sorted order
    Swap adjacent items that are out of order"""

    swap = False

    # loop through items in the list 
    for i in range(len(items)-1):
        # check if first item is greater than second
        if items[i] > items[i+1]:
            # if true, then swap the items' positions 
            items[i], items[i+1] = items[i+1], items[i]
            swap = True

    # keep iterating until there are no more swaps 
    if swap == True:
        items = bubble_sort(items)

    return items 


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2)
    Memory usage: O(1)

    Repeat until all items are in sorted order
    Find minimum item in unsorted items
    Swap it with first unsorted item """

    # loop through items in list 
    for i in range(len(items)):
        min = i 
        # find minimum element in list 
        for j in range(i+1, len(items)):
            if items[min] > items[j]:
                min = j 
        # swap the new minimum item with the first element 
        items[i], items[min] = items[min], items[i]

    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n^2)
    Memory usage: O(1)

    Repeat until all items are in sorted order
    Take first unsorted item
    nsert it in sorted order in front of items"""
    
    # loop through items in list
    for i in range(len(items)):
        current = items[i]
        # if not at end of list and there is an unsorted element 
        while i > 0 and items[i-1] > current:
            items[i] = items[i-1] # move larger item to right 
            i = i-1
        # place smaller element in current position
        items[i] = current

    return items
