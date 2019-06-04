#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array: [int, str], item: (int, str)) -> int or None:
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array: [int, str], item: (int, str), index=0) -> int or None:
    # set index
    index = 0
    # case: item is found, return index
    if array[index] == item:
        return index
    else:
        # case: recursive call, increment index until item is found
        return linear_search_recursive(array, item, index + 1)


    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)
    


def binary_search_iterative(array: [int, str], item: (int, str)) -> int or None:
    # init values, get middle index as a whole num
    middle_index = len(array) // 2
    left = 0
    right = len(array)
    not_found = True

    while not_found:
        if item == array[middle_index]:
            not_found = False
            return middle_index
        if item > array[middle_index]:
            left = middle_index
        if item < array[middle_index]:
            right = middle_index
    
    return None

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array: [int, str], item: (int, str), left_index=0, right_index=None) -> int or None:
    # ! Continually split until middle_index becomes the item you want to find
    # ! Runtime = O(logn)

    # left and right will only be set once, updated left and right will be needed for recursive calls
    # middle_index must be based of update left and right
    if right_index == None:
        right_index = len(array) - 1 

    middle_index = (left_index + right_index) // 2

    if item == array[middle_index]:
        return middle_index
    
    # case: item does not exist in list
    if left_index >= right_index:
        return None
    
    # case: middle_index <= item <= right (RHS)
    if item > array[middle_index]:
        return binary_search_recursive(array, item, middle_index + 1, right_index)
    # case: left <= item <= middle_index (LHS)
    if item < array[middle_index]:
        return binary_search_recursive(array, item, left_index, middle_index)
    

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
