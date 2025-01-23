class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def postorder(node):
            if not node:
                return (0, math.inf)
            
            left_count, left_state = postorder(node.left)
            right_count, right_state = postorder(node.right)
            
            state = min(left_state, right_state)
            total_cameras = left_count + right_count
            
            if state==0: # children are not monitored
                return (total_cameras + 1, 1) # install camera in current node
            
            if state==1: # one of the children is monitored and has camera
                return (total_cameras, 2) # set current node state as monitored but no camera
            
            return (total_cameras, 0) # set current node as unmonitored
        
        temp=TreeNode(0,root)
        return postorder(temp)[0]            