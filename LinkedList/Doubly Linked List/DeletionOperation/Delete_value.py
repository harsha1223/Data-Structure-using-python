class Node:
    def __init__(self, data):
        self.data = data
        self.nextreference = None
        self.previousreference = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        print()
        if (self.head is None):
            print('Linked List Is Empty!')
        else:
            n = self.head
            while(n is not None):
                print(n.data, '-->', end=" ")
                n = n.nextreference

    def print_LL_reverse(self):
        print()
        if (self.head is None):
            print('Linked List Is Empty!')
        else:
            n = self.head
            while(n.nextreference is not None):
                n = n.nextreference
            while(n is not None):
                
                print(n.data, '-->', end=" ")
                n = n.previousreference

    def insert_LinkedListEmpty(self, data):
        if (self.head is None):
            new_node = Node(data)
            self.head = new_node
        else:
            ('Linked List is not empty!')

    def add_beginning(self, data):
        new_node = Node(data)
        if (self.head is None):
            self.head = new_node
        else:
            new_node.nextreference = self.head
            self.head.previousreference = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if (self.head is None):
            self.head = new_node
        else:
            n = self.head
            while(n.nextreference is not None):
                n = n.nextreference
            n.nextreference = new_node
            new_node.previousreference = n

    def add_after(self,data,x):
        if(self.head is None):
            print('Linked list is empty')
        else:
            n = self.head
            while (n is not None):
                if(x==n.data):
                    break
                n = n.nextreference
            if (n is None):
                print('Given Node is not present in the given Linked List')
            else:
                new_node = Node(data)
                new_node.nextreference = n.nextreference
                new_node.previousreference = n
                if (n.nextreference is not None):
                    n.nextreference.previousreference = new_node
                n.nextreference = new_node

    def add_before(self,data,x):
        if(self.head is None):
            print('Linked list is empty')
        else:
            n = self.head
            while (n is not None):
                if(x==n.data):
                    break
                n = n.nextreference
            if (n is None):
                print('Given Node is not present in the given Linked List')
            else:
                new_node = Node(data)
                new_node.nextreference = n
                new_node.previousreference = n.previousreference
                if( n.previousreference is not None):
                    n.previousreference.nextreference = new_node
                else:
                    self.head = new_node
                n.previousreference = new_node

    def delete_beginning(self):
        if(self.head is None):
            print('Linked List is empty so we can not delete the given node')
            return
        if (self.head.nextreference is  None):
            self.head = None
            print('The given linked list is empty after deleting the given node')
        else:
            self.head = self.head.nextreference
            self.head.previousreference = None

    def delete_end(self):
        if(self.head is None):
            print('Linked List is empty so we can not delete the given node')
            return
        if (self.head.nextreference is  None):
            self.head = None
            print('The given linked list is empty after deleting the given node')
        else:
            n = self.head
            while(n.nextreference is not None):
                n = n.nextreference
            n.previousreference.nextreference = None

    def delete_by_value(self,x):
        if(self.head is None):
            print('Linked List is empty so we can not delete the given node')
            return
        if (self.head.nextreference is None):
            if(x==self.head.data):
                self.head = None
            else:
                print('X is not present in the linked list')
            return
        if (self.head.data==x):
            self.head = self.head.nextreference
            self.head.previousreference = None
            return
        n=self.head
        while (n.nextreference is not None):
            if (x == n.data):
                break
            n=n.nextreference
        if (n.nextreference is not None):
            n.nextreference.previousreference = n.previousreference
            n.previousreference.nextreference=n.nextreference
        else:
            if n.data == x:
                n.previousreference.nextreference = None
            else:
                print('X is notpresent in the Linked List.')
LL1 = DoublyLinkedList()
LL1.add_end(20)
LL1.delete_by_value(20)
LL1.print_LL()