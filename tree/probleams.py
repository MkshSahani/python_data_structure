# probleams.py 

import Queue 
import BST 
import random 
import Stack 

# do the levelorder traversal using Queue : concept of BFS is used. 
def levelOrderTraversal(node):
    node = node.root 
    if node is None:
        return
    
    # if tree is not a null tree do the following 
    queue = Queue.Queue()
    queue.enqueue(node)
    print()
    while not queue.isempty():
        node = queue.dequeue()
        # print(node)
        print(f"{node.key}", end = ' ')
        if node.left is not None:
            queue.enqueue(node.left)
        if node.right is not None:
            queue.enqueue(node.right)
        # print(queue.queue)
    print()


def getMaximum(node): # get the maximum key value in the binary tree. 
    temp = node
    while temp.right is not None:
        temp = temp.right
    return temp.key 


# def getMin(nodde)
def getMin(node):  # get the minimum value in the binary search tree. 
    if node is None:
        return None
    min = node.key
    queue = Queue.Queue()
    queue.enqueue(node)
    while not queue.isempty():  # traverse all the nodes in the binary tree. 
        node = queue.dequeue()
        min = min if min < node.key else node.key
        if node.left is not None:
            queue.enqueue(node.left)
        if node.right is not None:
            queue.enqueue(node.right)
    return min 

def getMax(node):  # get the maximum without using the recursion
    if node is None:
        return None

    queue = Queue.Queue()
    queue.enqueue(node)
    max = node.key
    while not queue.isempty():
        node = queue.dequeue()
        max = max if max > node.key else node.key
        if node.left is not None:
            queue.enqueue(node.left)
        if node.right is not None:
            queue.enqueue(node.right)
    return max  

def size(node):  # find the size : number of node in the binary tree using reursion :
    if node is None:
        return 0
    return size(node.left) + size(node.right) + 1 

# find the size of node without using the recursion

def getSize(node):
    if node is None:
        return 0
    queue = Queue.Queue()
    count = 0
    queue.enqueue(node)
    while not queue.isempty():
        temp = queue.dequeue()
        count += 1
        if temp.left is not None:
            queue.enqueue(temp.left)
        if temp.right is not None:
            queue.enqueue(temp.right)

    return count 

if __name__ == '__main__':
    bst = BST.BST()
    for i in range(20):
        # time.sleep(0.5)
        bst.insertNode(random.randint(1, 100))
    levelOrderTraversal(bst)
    print("The size of binary tree  is  ", size(bst.root))  # print the number node in give tree.
    print("The size of binary tree is : ", getSize(bst.root)) # get the size of binary tree. 