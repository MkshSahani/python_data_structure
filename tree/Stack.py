# Stack.py 

class Stack:
    
    def __init__(self):
        self.stack = []
        
    def push(self, element):
        self.stack.insert(0, element)
    
    def pop(self):
        if self.isempty():
            raise ValueError("Stack UnderFlow")
        else:
            return self.stack.pop(0)

    def isempty(self):
        return self.stack == []

    def top(self):
        if self.isempty():
            raise ValueError("Stack underflow")
        else:
            return self.stack[0]

    