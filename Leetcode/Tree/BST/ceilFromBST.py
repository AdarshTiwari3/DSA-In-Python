from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

def findCeil(root, x):
    # Write your code here.
    
    ceil = -1
    while root:
        if root.data==x:
            return root.data

        elif root.data<x:
            #move right
            root=root.right
        else:
            ceil=root.data
            root=root.left

    return ceil