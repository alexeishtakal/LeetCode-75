# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if root:
            if not root.left and not root.right:
                return [root.val]
            res = []
            if root.left:
                l = self.dfs(root.left)
                res.extend(l)
            if root.right:
                r = self.dfs(root.right)
                res.extend(r)
            return res

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a = self.dfs(root1)
        b = self.dfs(root2)
        return a == b