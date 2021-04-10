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

# root = BST(None)      
# root.insert(20)  
root = BST(10)      
root.insert(20)  