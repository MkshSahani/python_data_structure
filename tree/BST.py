# BST.py 

import random 
import time  

class Node: 

    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None
        
    def __str__(self):
        print_string = f"Node data : {self.key} left : {id(self.left)} right : {id(self.right)}"
        return print_string
    
class BST:
    
    def __init__(self):
        self.root = None
        
    def insertNode(self, key):
        if self.root is None:
            self.root = Node()
            self.root.key = key
        else:
          self.insert(self.root, key)

    def insert(self, node, key):
        if node is None:
            node = Node()
            node.key = key
        else:  
            if key >= node.key:
                node.right = self.insert(node.right, key)
            else:
                node.left = self.insert(node.left, key)
        return node
    
    def printTree(self):
        self.inorderTraversal(self.root)
    
    def inorderTraversal(self, node):
        if node is not None:
            self.inorderTraversal(node.left)
            print(f"{node.key} ", end='')
            self.inorderTraversal(node.right)

    def preorderPrint(self):
        self.preorderTraversal(self.root)

    def preorderTraversal(self, node):
        if node is not None:
            print(f"{node.key} ", end='')
            self.preorderTraversal(node.left)
            self.preorderTraversal(node.right)

    def height(self):
        return self.getheight(self.root)
    
    def getheight(self, node):
        if node is None:
            return -1
        else:
            rh = self.getheight(node.right) + 1
            lh = self.getheight(node.left) + 1
            return rh if rh > lh else lh 

def size(root):  # find the number of node in the binary tree.
    if root is None:
        return 0
    return size(root.left) + size(root.right) + 1 


if __name__ == '__main__':
    bst = BST()
    for i in range(20):
        # time.sleep(0.5)
        bst.insertNode(random.randint(1, 100))
    print(bst.root)
    bst.printTree()
    print()
    bst.preorderPrint()
    print()
    print("Height of the Binary Search Tree : ", bst.height())
    print()
    print("Number  of node in the given tree is ", size(bst.root))