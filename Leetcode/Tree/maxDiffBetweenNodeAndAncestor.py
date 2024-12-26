class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, maxi, mini):
            nonlocal ans
            if node is None:
                return
            maxi=max(maxi,node.val)
            mini=min(mini,node.val)
            
            ans = max(ans, abs(maxi - mini))
            print("ans->",ans)
            dfs(node.left, maxi,mini )
            dfs(node.right, maxi, mini)

        dfs(root, root.val, root.val)
        return ans