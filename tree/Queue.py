# Queue.py  

class Queue:
    
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isempty():
            raise ValueError("Queue Underflow")
        else:
            return self.queue.pop(0)
    
    def isempty(self):
        self.queue == []

    def front(self):
        if self.isempty():
            raise ValueError("Queue UnderFlow")
        else:
            return self.queue[0]

