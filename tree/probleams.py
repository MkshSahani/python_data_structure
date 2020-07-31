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

# get the level order reversed.

def reverseLevelOrder(node):
    if node is None:
        return False
    
    queue = Queue.Queue()
    queue.enqueue(node)
    stack = Stack.Stack()

    while not queue.isempty():
        temp = queue.dequeue()
        stack.push(temp)
        if temp.left is not None:
            queue.enqueue(temp.left)
        if temp.right is not None:
            queue.enqueue(temp.right)

    while not stack.isempty():
        print(stack.pop().key, end = ' ')

def height(node):
    if node is None:
        return -1
    lh = height(node.left) + 1
    rh = height(node.right) + 1
    return lh if lh > rh else rh 


def preorderTraversal(node):
    if node is not None:
        print(node.key, end=' ')
        preorderTraversal(node.left) 
        preorderTraversal(node.right) 

def inorderTraversal(node):
    if node is not None:
        inorderTraversal(node.left)
        print(node.key, end=' ')
        inorderTraversal(node.right)


def getHeight(node):
    if node is None: 
        return False
    else:
        marker = BST.Node()
        node.key = 323233223
        queue = Queue.Queue()
        queue.enqueue(node)
        queue.enqueue(marker)
        count = -1
        while not queue.isempty(): 
            temp = queue.dequeue()
            if temp == marker:
                count += 1 
                if not queue.isempty(): 
                    queue.enqueue(marker)
            else: 
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
    # levelOrderTraversal(bst)
    # print("The size of binary tree  is  ", size(bst.root))  # print the number node in give tree.
    # print("The size of binary tree is : ", getSize(bst.root))  # get the size of binary tree.
    # reverseLevelOrder(bst.root)
    # print()
    inorderTraversal(bst.root)
    print()
    preorderTraversal(bst.root)
    print() 
    print("Height of tree : ", height(bst.root)) # get the height of tree. 
    print("Height of tree : ", getHeight(bst.root)) # get  the height of tree. 
