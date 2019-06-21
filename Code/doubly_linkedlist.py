#!python
from node import Node

class DoublyLinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes

        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """
        Return the length of this linked list by traversing its nodes
        """
        return self.size

    def get_at_index(self, index: int):
        """
        Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        """
        # ! Runtime best & worst = O(n), n being the size of index

        if not (0 <= index < self.size):
            raise ValueError(f'index {index} is out of range for Linked List!')
    
        # start at head
        node = self.head

        # iterate through pointers of ll by input index
        for _ in range(index):
            node = node.next
        
        return node.data
    def node_at_index(self, index: int):
        """
        Returns node at given index of linked list, or raises 
        ValueError if the given index is out of range of the list size.
        """ 

        # ! Runtime best and worst = O(n), n being index.

        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        
        # init node
        node = self.head

        # loop through ll
        for _ in range(index):
            node = node.next
        
        return node

    def insert_at_index(self, index, item):
        """
        Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        """

        # ! Runtime best = O(1)
        # ! Runtime worst = O(2n), node_at_index() called. Tends to O(n) -> scales linearly.   

        if not (0 <= index <= self.size):
            raise ValueError(f'index {index} is out of range for Linked List!')

        # case: insert new node as head with a dll size > 1
        if index == 0:
            self.prepend(item)

        # case: insert new node as tail
        elif index == self.size:
            self.append(item)
        
        else:
            # init nodes
            index_node = self.node_at_index(index)
            previous_node = index_node.previous
            new_node = Node(item)
            # update pointers
            new_node.next = index_node
            new_node.previous = previous_node
            index_node.previous = new_node
            previous_node.next = new_node
            # update size
            self.size += 1
        
    def append(self, item):
        """
        Insert the given item at the tail of this linked list.
        """
        # ! Runtime best & worst = O(1), given that tail is the end of ll. 
        
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
            self.size += 1
        else:
            # Otherwise insert new node after tail
            self.tail.next = new_node
            new_node.previous = self.tail
            self.size += 1
        # Update tail to new node regardless
        self.tail = new_node

    def prepend(self, item):
        """
        Insert the given item at the head of this linked list.
        """

        # ! Runtime best & worst = O(1), given that head is the front of ll. 

        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.head = self.tail = new_node
            self.size += 1
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
            self.head.previous = new_node
            self.size += 1
        # Update head to new node regardless
        self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """
        Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        """
        
        # ! Runtime best = O(1). 
        # ! Runtime worst = O(n), n being size/length of ll. 

        node = self.head
        for _ in range(self.size):
            if node.data == old_item:
                node.data = new_item
                return 
            node = node.next
        # node not found
        raise ValueError

    def delete(self, item):
        """
        Delete the node containing the first occurrence of the given item in this linked list,
        or raise ValueError if given item is not found.
        """
        # ! Runtime best = O(1)
        # ! Runtime worst = O(n), n being the size/length of ll. 

        # case: empty dll
        if self.size < 1:
            raise ValueError(f'Linked List size is {self.size}!')
        
        # case: dll only has one node
        if self.size == 1:
            if self.head.data == item:
                self.head = None
                self.tail = None
                self.size -= 1
                return  # exit early because deletion is done
            else:
                raise ValueError(f'{item} is not in doubly linked list!')
        
        # remaining cases: dll has >= 2 nodes
        # case: item is in head
        if self.head.data == item:
            node = self.head
            next_node = node.next
            self.head = next_node
            # unlink both nodes
            next_node.previous = None
            node.next = None
            self.size -= 1
            return  # exit early because deletion is done
        # case: item is in tail
        if self.tail.data == item:
            node = self.tail
            previous_node = node.previous
            # unlink both nodes
            previous_node.next = None
            node.previous = None
            self.tail = previous_node
            self.size -= 1
            return  # exit early because deletion is done

        # remaining cases: dll has >= 2 nodes and item is not in head or tail
        # start at node after head
        node = self.head.next

        # iterate through dll whos size is >= 2
        while node is not None:
            if node.data == item:
                previous_node = node.previous
                next_node = node.next
                # update links to point around this node
                previous_node.next = next_node
                next_node.previous = previous_node
                self.size -= 1
                return  # exit early because deletion is done
            # advance one node down the chain
            node = node.next
        
        raise ValueError(f"{item} not found in doubly linked list!")

def test_linked_list():
    ll = DoublyLinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
