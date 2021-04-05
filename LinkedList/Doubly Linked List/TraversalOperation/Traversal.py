class Node:
    def __init__(self, data):
        self.data = data
        self.nextreference = None
        self.previousreference = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if (self.head is None):
            print('Linked List Is Empty!')
        else:
            n = self.head()
            while(n is not None):
                print(n.data, '-->', end=' ')
                n = n.nextreference

    def print_LL_reverse(self):
        if (self.head is None):
            print('Linked List Is Empty!')
        else:
            n = self.head()
            while(n.nextreference is not None):
                n = n.nextreference
            while(n is not None):
                print(n.data, '-->', end=' ')
                n = n.previousreference

LL1 = DoublyLinkedList()
LL1.print_LL()