# BST.py 

class Node: 

    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None
        
    def __str__(self):
        print_string = f"Node data : {self.key} left : {id(self.left)} right : {id(self.right)}"
        return print_string
    

if __name__ == '__main__':
    node = Node()
    node.key = 3
    print(node)
        