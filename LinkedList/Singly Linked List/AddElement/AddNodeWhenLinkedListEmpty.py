class Node:
    def __init__(self, data):
        self.data = data
        self.reference = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if (self.head is None):
            print('Linked List is Empty!')
        else:
            n = self.head
            while (n is not None):
                print(n.data, '-->', end=' ')
                n = n.reference

    def atBeginning(self, data):
        new_node = Node(data)
        new_node.reference = self.head
        self.head = new_node

    def atEnd(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
        else:
            n = self.head
            while (n.reference is not None):
                n = n.reference
            n.reference = new_node

    def add_after_given_node(self, data, x):
        n = self.head
        while (n is not None):
            if (x == n.data):
                break
            n = n.reference
        if (n is None):
            print('Node is not present in the given Linked List')
        else:
            new_node = Node(data)
            new_node.reference = n.reference
            n.reference = new_node

    def add_before_given_node(self, data, x):
        if (self.head == None):
            print("Linked list is empty!")
            return
        if (self.head.data == x):
            new_node = Node(data)
            new_node.reference = self.head
            self.head = new_node
            return
        n = self.head
        while(n.reference is not None):
            if (n.reference.data==x):
                break
            n = n.reference
        if (n.reference is None):
            print('Node not found')
        else:
            new_node = Node(data)
            new_node.reference = n.reference
            n.reference= new_node
    def insert_empty(self,data):
        if(self.head is None):
            new_node = Node(data)
            self.head = new_node
        else:
            print('Linked List is not empty!')

LL1 = LinkedList()
LL1.insert_empty(20)
LL1.isEmpty()