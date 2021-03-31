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
                print(n.data)
                n = n.reference

    def atBeginning(self, data):
        new_node = Node(data)
        new_node.reference = self.head
        self.head = new_node


LL1 = LinkedList()
LL1.atBeginning(20)
LL1.atBeginning(10)
LL1.isEmpty()