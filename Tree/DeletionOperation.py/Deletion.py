class BST:
    def __init__(self , key):
        self.key = key
        self.leftchild = None
        self.rightchild = None
    
    def insert(self,data):
        if (self.key is None):
            self.key = data
            return
        if (self.key == data):
            return
        if (self.key > data):
            if (self.leftchild):
                self.leftchild.insert(data)
            else:
                self.leftchild = BST(data)
        else:
            if (self.rightchild):
                self.rightchild.insert(data)
            else:
                self.rightchild = BST(data)

    def search(self,data):
        if (self.key == data):
            print('Node is found')
            return
        if (self.key > data):
            if (self.leftchild):
                self.leftchild.search(data)
            else:
                print('Node is not present in tree!')

        else:
            if self.rightchild:
                self.rightchild.search(data)
            else:
                print('Node is not present in tree!')

    def preordertraversal(self):
        print(self.key,end = ' ')
        if (self.leftchild):
            self.leftchild.preordertraversal()
        if self.rightchild:
            self.rightchild.preordertraversal()
    
    def inordertraversal(self):
        if (self.leftchild):
            self.leftchild.inordertraversal()
        print(self.key,end =' ')
        if (self.rightchild):
            self.rightchild.inordertraversal()  

    def postordertraversal(self):
        if (self.leftchild):
            self.leftchild.postordertraversal()
        if (self.rightchild):
            self.rightchild.postordertraversal() 
        print(self.key,end =' ') 

    def delete(self,data):
        if (self.key is None):
            print('Tree is empty')
            return
        if (data < self.key):
            if (self.leftchild):
                self.leftchild = self.leftchild.delete(data)
            else:
                print('Given Node is not present in the tree.')
        elif(data>self.key):
            if (self.rightchild):
                self.rightchild = self.rightchild.delete(data)
            else:
                print('Given Node is not present in the tree.')
        else:
            if(self.leftchild is None):
                temp = self.rightchild
                self = None
                return temp
            if(self.rightchild is None):
                temp = self.leftchild
                self = None
                return temp
            node = self.rightchild
            while (node.leftchild):
                node = self.leftchild
            self.key = node.key
            self.rightchild = self.rightchild.delete(node.key)
        return self


root = BST(10)
list1 = [6,3,1,6,98,3,7]
for i in list1:
    root.insert(i)
print('Pre-Order')
root.preordertraversal()
print()
root.delete(6)
print('after deleting')
root.preordertraversal()