# BST.py 

import random 

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
            
    def insert(self, node, key):
        if node is Node:
            node = Node()
            node.key = key
        
        if key >= node.key:
            self.insert(node.right, key)
        else:
            self.insert(node.left, key)

    
    def printTree(self):
        pass
    
    def inorderTraversal(self, node):
        if node is None:
            self.inorderTraversal(node.left)
            print(f"{node.key} ", end=" ")
            self.inorderTraversal(node.right)



if __name__ == '__main__':
    pass
