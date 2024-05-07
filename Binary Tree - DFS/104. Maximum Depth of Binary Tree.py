# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if root:
            ld = self.dfs(root.left)
            rd = self.dfs(root.right)
            depth = max(ld, rd) + 1
            return depth
        else:
            return 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
