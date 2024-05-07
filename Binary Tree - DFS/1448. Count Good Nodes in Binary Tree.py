# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, prev_val):
        if node:
            if node.left:
                gl = self.dfs(node.left, max(node.val, prev_val))
            else:
                gl = 0

            if node.right:
                gr = self.dfs(node.right, max(node.val, prev_val))
            else:
                gr = 0

            current_count = 0
            if node.val >= prev_val:
                current_count = 1
            return gl + gr + current_count

        else:
            return 0

    def goodNodes(self, root: TreeNode) -> int:
        if root.left or root.right:
            return self.dfs(root, root.val)
        else:
            return 1
