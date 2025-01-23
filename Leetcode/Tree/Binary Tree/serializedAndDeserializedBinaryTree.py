# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue=deque([root])
        string=""
        while queue:
            node=queue.popleft()
            if node is None:
                string+="*,"
            else:
                string+=str(node.val)+','
                queue.append(node.left)
                queue.append(node.right)
        # print("string=",string)
        return string

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not len(data):
            return None

        string=data.split(',')
        if string[0]=='*':
            return None
        root=TreeNode(int(string[0]))
        queue=deque([root])
        idx=1 # as zero already process 
        while queue:
            node=queue.popleft()
            #create left and right child
            if string[idx] != '*':
                node.left=TreeNode(int(string[idx])) 
                #push into the queue to process next level
                queue.append(node.left)
            else:
                node.left=None
            idx+=1
            if string[idx]!='*':
                node.right=TreeNode(int(string[idx]))
                queue.append(node.right)
            else:
                node.right=None
            idx+=1
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))