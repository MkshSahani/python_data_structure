# singlyLinkedList.py 

import random 

class Node: 
    def __init__(self): 
        self.key = None 
        self.link = None 



class List:
    
    def __init__(self):
        self.head = None
        
    def insertNode(self, key):
        if self.head is None:
            self.head = Node()
            self.head.key = key
        else:
            temp = self.head
            while temp.link is not None:
                temp = temp.link
            temp.link = Node()
            temp.link.key = key

    def printList(self):
        temp = self.head
        print("List : ")
        while temp.link is not None:
            print(temp.key, end = ' ')    
            temp = temp.link
            


if __name__ == '__main__':
    # singlyLinkedList implementation
    list = List()
    for i in range(10):
        list.insertNode(random.randint(1, 100))
    list.printList() # print the list. 