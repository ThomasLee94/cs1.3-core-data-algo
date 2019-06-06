#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array: [int, str], item: (int, str)) -> (int, None):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array: [int, str], item: (int, str), index=0) -> (int, None):
    # case: index exceeds length of array, item does not exist in array
    if index >= len(array):
        return None

    if array[index] == item:
        return index
    
    # case: increment index until item is found
    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)
    

def binary_search_iterative(array: [int, str], item: (int, str)) -> (int, None):
    # ! Continually split until middle_index becomes the item you want to find
    # ! Runtime = O(logn)

    # left and right will only be set once, updated left and right will be needed for while loop
    left_index = 0
    right_index= len(array) - 1
    
    # left_index should never == right_index
    while left_index != right_index:
        # middle_index must be based of update left and right
        middle_index = (left_index + right_index) // 2

        if item == array[middle_index]:
            return middle_index
        # case: middle_index <= item <= right (RHS)
        # + 1 is needed to update left_index as we are flooring, for the case for 2 elements in a list
        if item > array[middle_index]:
            left_index = middle_index + 1
        # case: left <= item <= middle_index (LHS)
        if item < array[middle_index]:
            right_index = middle_index 
    
    # case: item is last element in array
    if item == array[right_index]:
        return right_index
    
    # case: item does not exist in list
    return None

def binary_search_recursive(array: [int, str], item: (int, str), left_index=0, right_index=None) -> (int, None):
    # ! Continually split until middle_index becomes the item you want to find
    # ! Runtime = O(logn)

    # left and right will only be set once, updated left and right will be needed for recursive calls
    if right_index == None:
        right_index = len(array) - 1 

    # middle_index must be based of update left and right (floor)
    middle_index = (left_index + right_index) // 2
    
    # case: item does not exist in list
    if left_index >= right_index:
        return None
    
    if item == array[middle_index]:
        return middle_index
    
    # case: middle_index <= item <= right (RHS)
    # +1 is needed to update left_index as we are flooring, for case: 2 elements in a list
    if item > array[middle_index]:
        return binary_search_recursive(array, item, middle_index + 1, right_index)
    # case: left <= item <= middle_index (LHS)
    if item < array[middle_index]:
        return binary_search_recursive(array, item, left_index, middle_index)
    
