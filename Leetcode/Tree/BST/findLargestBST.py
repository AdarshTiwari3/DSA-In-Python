'''

    ------- Binary Tree node structure -------
            class TreeNode :
                def __init__(self, data) :
                    self.data = data
                    self.left = None
                    self.right = None

'''
import math
def largestBST(root):

	# Write your code here.
    def helper(root):
        if root is None:
            return math.inf,-math.inf,0 #(min,max,size)
        
        leftMin,leftMax,leftSize=helper(root.left)
        rightMin,rightMax,rightSize=helper(root.right)

        if not leftMax<root.data<rightMin:
            #invailid BST
            return -math.inf,math.inf,max(leftSize,rightSize)
        return min(root.data,leftMin),max(root.data,rightMax),leftSize+rightSize+1



    ans=helper(root)[2] # because it is touple of min max size
    return ans