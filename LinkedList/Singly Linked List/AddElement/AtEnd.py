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
                print(n.data , "-->" ,end = " ")
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

LL1 = LinkedList()
LL1.atBeginning(10)
LL1.atBeginning(20)
LL1.atEnd(30)
LL1.atEnd(60)
LL1.isEmpty()