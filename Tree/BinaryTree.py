class BST:
    def __init__(self , key):
        self.key = key
        self.leftchild = None
        self.rightchild = None

        
root = BST(10)
print(root.key)
print(root.leftchild)
print(root.rightchild)

root.leftchild = BST(5)
print(root.key)
print(root.leftchild)
print(root.leftchild.key)
print(root.rightchild)
