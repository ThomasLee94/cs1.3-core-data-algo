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

    def is_empty(self) -> bool:
        """Return True if this stack is empty, or False otherwise."""
        print(self.list.size)

        if self.list.size < 1:
            return True
        return False

    def length(self) -> int:
        """Return the number of items in this stack."""
        
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack."""

        # ! Runtime = O(1)
        
        return self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        
        if self.is_empty():
            return None
        return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty."""

        # ! Runtime = O(1)
        
        if self.list.size == 0:
            raise ValueError("Stack is empty")

        output_data = self.list.head.data
        self.list.delete(output_data)
        return output_data


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

        if len(self.list) < 1:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""

        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack."""

        # ! Runtime = O(1)
        
        return self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""

        if self.is_empty():
            return None
        return self.list[len(self.list) - 1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty."""

        # ! Runtime = O(1)
        
        if self.is_empty():
            raise ValueError("Stack is empty")
        
        output_item = self.list[len(self.list) - 1]
        del self.list[len(self.list) - 1]
        return output_item


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
