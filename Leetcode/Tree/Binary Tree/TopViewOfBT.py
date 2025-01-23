from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)

# Following is the TreeNode class structure:
from collections import deque
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def getTopView(root):
    # Write your code here.
    if root is None:
        return []
    
    queue=deque([(root,0)])
    seen={} # this will be used as a visited array like vertical order traversal , only insert the first element of that column

    while queue:
        node,col=queue.popleft()
        if node.left:
            queue.append((node.left,col-1))
        if node.right:
            queue.append((node.right,col+1))
        # check if the column has been visited or not, if not then only insert 
        if col not in seen:
            seen[col]=node.val
    top_view=[seen[col] for col in sorted(seen.keys())]
    return top_view
# Taking input.
def takeInput():

    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1):
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()

        leftChild = arr[index]

        if(leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if(rightChild != -1):
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)

        index += 1

    return root

# Printing the tree nodes.
def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()


# Main.
T = 1
for i in range(T):
    root = takeInput()
    ans = getTopView(root)
    printAns(ans)