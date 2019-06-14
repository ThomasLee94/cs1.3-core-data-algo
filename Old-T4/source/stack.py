#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # ll class method
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        return self.list.length()

    # ─── TOP IS HEAD ─────────────────────────────────────────────────

    # ─── BOTTOM IS TAIL ──────────────────────────────────────────────

    def push(self, item):
        """Insert the given item on the top of this stack."""
        # ! Best & worst case runtime = O(1), not dependent on length of ll

        # append node to the tail
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        
        # case: tail node is empty
        if self.list.is_empty():
            return None
        # return tail data
        return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty."""

        # ! Worst & best case runtime = O(1), not dependent on length of ll
        
        # case: ll length is 0
        if self.list.length() == 0:
            raise ValueError('Linked list length is 0')
        # case: top node is empty
        if self.list.is_empty():
            raise ValueError("Node is empty")
        # delete tail node
        item = self.list.head.data
        self.list.delete(item)
        return item

# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        if len(self.list) == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        
        return len(self.list)


    # ─── END OF LIST IS TOP ─────────────────────────────────────────────────────────

    # ─── START OF LIST IS BOTTOM ────────────────────────────────────────────────────


    def push(self, item):
        """Insert the given item on the top of this stack."""
        # ! Best & worst case runtime = O(1), not dependent on size of list

        # insert new item at the end of the list
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        
        # case: list is empty
        if len(self.list) == 0:
            return None
        # show last element
        last_index = len(self.list) - 1
        return self.list[last_index]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty."""

        # case: list length is 0
        if len(self.list) == 0:
            raise ValueError("list length is 0")
        # remove last index (top)
        last_index = len(self.list) - 1
        top_element = self.list.pop(last_index)
        return top_element




# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
