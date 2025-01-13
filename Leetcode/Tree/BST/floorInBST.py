from os import *
from sys import *
from collections import *
from math import *


def floorInBST(root, X):
    floor = -1
    while root:
        if root.data == X:
            floor = root.data
            return floor
        if root.data < X:
            floor=root.data
            root=root.right
        else:
            root=root.left
    return floor