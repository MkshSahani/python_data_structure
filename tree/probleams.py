# probleams.py 

import Queue 
import BST 
import random 

# do the levelorder traversal using Queue : concept of BFS is used. 
def levelOrderTraversal(node):
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




if __name__ == '__main__':
    bst = BST.BST()
    for i in range(20):
        # time.sleep(0.5)
        bst.insertNode(random.randint(1, 100))
    print(bst.root)
    bst.printTree()
    levelOrderTraversal(bst.root)
