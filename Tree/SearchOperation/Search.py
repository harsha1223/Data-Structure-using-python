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

root = BST(10)
list1 = [6,3,1,6,98,3,7]
for i in list1:
    root.insert(i)
root.search(60)