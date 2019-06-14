#!python

def linear_search(array: [int, str], item: (int, str)) -> (int, None):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array: [int, str], item: (int, str)) -> (int, None):
    """ 
    loop over all array values until item is found -> iterative
    return: index int, None
    """
    # ! O(n)
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array: [int, str], item: (int, str), index = 0) -> (int, None):
    """ 
    loop over all array values until item is found -> recursive 
    return: index int, None
    """
    # ! O(n)
    # case: index is out of bounds
    if index >= len(array):
        return None 
    # case: item matches array[index] -> return index int
    elif item == array[index]:
        return index
    # case: recursion for when item is not found, increment index 
    else:
        return linear_search_recursive(array, item, index + 1)

def binary_search(array: [int, str], item: (int, str)) -> (int, None):
    """
    return the index of item in sorted array or None if item is not found
    """
    # ! O(log2N)
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array: [int, str], item: (int, str)) -> (int, None):
    """ 
    loop over given sorted array values until item is found 
    """
    # ! continually split until the item becomes the middle index
    # get middle index (odd and even list length)
    first_index = 0
    last_index = len(array) - 1
    while first_index != last_index: 
        middle_index = (first_index + last_index) // 2
        # case: if item is in the middle
        if array[middle_index] == item:
            return middle_index
        # case: if item is smaller, search first_index <= x <= middle_index 
        elif array[middle_index] > item:
            # update last index
            last_index = middle_index - 1
        # case: if item is greater, search middle_index <= x <= last_index
        elif array[middle_index] < item:
            # update first index
            first_index = middle_index + 1 
    # case: item found as last element
    if array[last_index] == item:
        return last_index
    # case: item not found
    else:
        return None


def binary_search_recursive(array: [int, str], item: (int, str), left=None, right=None) -> (int, None):
    # ! continually split until the item becomes the middle index
    # case: left == right 
    if left == right and left is not None:
        # case: traverse binary search from any direction and item is not found
        if left == len(array):
            return None
        # case: check if index is item
        elif array[left] == item:
            return left
        # case: item not found
        else:
            return None
    # case: binary search
    if left == None and right == None:
        left = 0
        right = len(array) 
    # set middle index
    middle_index = (left + right) // 2
    # checks with either side of middle_index
    if array[middle_index] == item:
        return middle_index
    # case: check 0 <= x <= middle_index
    elif array[middle_index] > item:
        right = middle_index - 1 
    # case: check middle_index <= x <= right
    elif array[middle_index] < item:
        left = middle_index + 1 
    return binary_search_recursive(array, item, left, right)
