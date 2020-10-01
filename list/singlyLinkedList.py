# singlyLinkedList.py 

import random 

# Node the building block of LinkedList. 
class Node:
    
    def __init__(self): 
        self.key = None # key value of Node. 
        self.link = None # link to the next node. 


# Singly LinkedLists. 
class List:
    
    def __init__(self):
        self.head = None
        
    def insertNode(self, key): # insert node at the end of linked List. 
        if self.head is None:
            self.head = Node()
            self.head.key = key
        else:
            temp = self.head
            while temp.link is not None:
                temp = temp.link
            temp.link = Node()
            temp.link.key = key

    def printList(self): # print Linked List. 
        temp = self.head
        print("List : ", end = '')
        while temp.link is not None:
            print(temp.key, end = ' ')    
            temp = temp.link
        print()

    def deleteNode(self, key):
        temp = self.head
        previous = temp
        while temp is not None and temp.key != key:
            previous = temp
            temp = temp.link
        
        if temp is not None:
            if temp == self.head:
                self.head = self.head.link
            else:
                previous.link = temp.link 

    def search(self, key):
        temp = self.head
        while temp != None and temp.key != key:
            temp = temp.link         
        if temp != None:
            return temp.key, True

if __name__ == '__main__':
    # singlyLinkedList implementation
    list = List()
    for i in range(30):
        list.insertNode(random.randint(1, 100))
    list.printList()  # print the list.
    for i in range(4):
        key = int(input())
        list.deleteNode(key)
        list.printList()  # print the modified list.
    
