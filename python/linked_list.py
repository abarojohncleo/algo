class Node:
    """
    An object for sorting a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class linkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes 0(n) time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        
        return count

    def add(self, data):
        """
        Adds new Node containing data at head of the list
        Takes 0(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def searchSelf(self, key):
        """
        Searches for first node containing data that matches given key
        Return node of None if not found
        Takes 0(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insertData(self, data, index):
        """
        Inserts a new Node containing data and index position
        Insertion takes 0(1) time but finding the node at the insertion point takes 0(n) time

        Takes overall 0(n) time
        """

        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data) 

            position = index
            current =self.head

            while position > 1:
                current = current.next_node
                position -=1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def removeData(self, key):
        """
        Removes node that matches the key
        Returns node or None if not exists
        
        Takes 0(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current
        
    def __repr__(self):
        """
        Returns a string representation
        Takes 0(n) time
        """

        nodes = []
        current = self.head

        while current:
            if current == self.head:
                nodes.append("[Head: %s]" %current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" %current.data)
            else:
                nodes.append("[%s]" %current.data)

            current = current.next_node
        return '-> '.join(nodes)