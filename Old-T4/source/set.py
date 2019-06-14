from hashtable import HashTable
class Set:
  
  def __init__(self, elements=None):
    """ init set """
    # ! size of set can be found as attribute in hashtable class 

    # using hastable class to have the ability to pass elements in as an array 
    self.data = HashTable()

    # if no elements are passed, init empty set. Else, fill set with individual element(s)
    if elements is not None:
      for element in elements:
        self.add(element)

  def length(self):
    """ return number of elements in set """
    return self.data.length()

  def return_elements(self):
    """ show all elements in current set """

    # ! Runtime = O(n), n is number of keys in hashtable

    return self.data.keys()
  
  def contains(self, element):
    """ if contains -> True, else False """

    # ! Runtime = O(1), key-value pairs - constant lookup with hashtable
    
    return self.data.contains(element)
  
  def add(self, element):
    """ add element in set if not already present """
    
    # ! Runtime = O(n), n is number of elements in set
    # ! element is not expected to already be in set, will tend towrads O(1)

    # case: unique item already an element in elements
    if self.data.contains(element):
      return
  
    # add element to set using hashtable class set method
    self.data.set(element, element) 

  def remove(self, element):
    """ remove element from set if present or raise KeyError""" 
    
    # keyError raised in hashtable delete method
    self.data.delete(element)
  
  def union(self, other_set):
    """ return union as set of this set and other_set  """
    
    # ! Runtime = O(n+m), n being the number of elements in set 1, m being the number
    # ! of elements in other_set

    # create empty set that will be filled with union elements
    union = Set()

    # search for all unique elements in current_set(self.elements) and other_set
    for item in self.data.keys():
      union.add(item)
    for item in other_set.data.keys():
      union.add(item)
    
    return union

  def intersection(self, other_set):
    """ return intersection as a new set between this set and other_set"""
    
    # ! Runtime = O(n*m),n being the number of elements in set 1, m being the number of elements in other_set
      
    intersection = Set()

    # case: set large and small set
    if self.data.length() > other_set.data.length():
      large = self.return_elements()
      small = other_set.return_elements()
    else:
      large = other_set.return_elements()
      small = self.return_elements()

    # case: search for all unique elements in both sets by checking the elements in large from small
    for element in small:
      if element in large:
        intersection.add(element)
    return intersection

  def difference(self, other_set):
    """ return a new set that is the diff of this set and other_set"""

    # ! Runtime = O(n*m),n being the number of elements in set 1, m being the number of elements in other_set

    diff = Set()

    # case: set large and small set
    if self.data.length() > other_set.data.length():
      large = self.return_elements()
      small = other_set.return_elements()
    else:
      large = other_set.return_elements()
      small = self.return_elements()

    # case: search for all unique elements not in both sets by checking the elements in large from small
    for element in small:
      if element not in large:
        diff.add(element)

    print(diff.length())
    return diff
  
  def is_subset(self, other_set):
    """ if other_set is subset -> True, else False"""

    # case: current_set is larger than other_set
    if self.data.length() > other_set.length():
      return False
    
    # loop through smaller set
    for element in self.return_elements():
      if not other_set.contains(element):
        return False
    
    # every element from other_set is in current_set as a subset
    return True