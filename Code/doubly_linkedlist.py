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

        if 0 <= index <= self.size:
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

        if 0 <= index <= self.size:
            raise ValueError(f'index {index} is out of range for Linked List!')

        # start at head
        node = self.head

        # iterate through pointers of ll by input index
        for _ in range(index):
            node = node.next
        
        return node
        

    def node_by_item(self, item):
        """
        Returns node that contains item
        """ 

        # ! Runtime best and worst = O(n), n being the length/size of ll. 
        # check head and tail
        if self.head.data == item:
            return self.head
        if self.tail.data == item:
            return self.tail

        try:
            # start at self.head.next
            node = self.head.next

            # while ll length is greater than 1
            while node.next is not None:
                if node.next.data == item:
                    return node.next 
                elif node.previous.data == item:
                    return node.previous
                node = node.next 
            
            return node

        # ll size = 1 
        except node as error:
            # item not in ll
            raise error

    def insert_at_index(self, index, item):
        """
        Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        """

        # ! Runtime best = O(1)
        # ! Runtime worst = O(2n), node_at_index() called. Tends to O(n) -> scales linearly.   
        try:
          # case: insert new node as head
          if index == 0:
              self.prepend(item)

          # case: insert new node as tail
          elif index == self.size:
              self.append(item)
          else:
              # init nodes
              index_node = self.node_at_index(index)
              previous_node = index_node.previous
              next_node = index_node.next
              new_node = Node(item)
              # update pointers
              new_node.next = index_node
              new_node.previous = previous_node
              previous_node.next = new_node
              next_node.previous = new_node
              # update size
              self.size += 1
        except:
            raise ValueError('List index out of range: {}'.format(index))

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
            self.tail = new_node
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
        
        pass

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
        Delete the node containing the given item in this linked list, or raise ValueError.
        """
        # ! Runtime best = O(1)
        # ! Runtime worst = O(n), n being the size/length of ll. 

        if self.size <= 1:
            raise ValueError(f'Linked List size is {self.size}!')
        
        # check head and tail
        if self.head.data == item:
            self.head.next = None
            self.head.next.previous = None
            self.size -= 1
        if self.tail.data == item:
            previous_node = self.tail.previous
            previous_node.next = None
            self.tail.previous = None
            self.size -= 1

        # start at self.head.next
        node = self.head.next

        # while ll length is greater than 1
        while node.next and node.next.next is not None:
            if node.next.data == item:
                next_node = node.next
                # set current node.next to skip next node
                node.next = next_node.next
                # set next_node.previous to skip current node
                next_node.previous = None
                # set next_node.next to skip node.next.next
                next_node.next = None
                # set next_node.next.previous to point to current node
                next_node.next.previous = node 
                # update size
                self.size -= 1
            elif node.previous.data == item:
                previous_node = node.previous
                # set current node.previous to skip previous node
                node.previous = previous_node.previous
                # set previous_node.next to skip current node
                previous_node.next = None
                # set previous_node.previous to skip node current node needs to point to
                previous_node.previous = None
                # set the now previous node from currents' next to point to current node
                node.previous.next = node
                # increment count
                self.size -= 1
            node = node.next.next 

       


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
