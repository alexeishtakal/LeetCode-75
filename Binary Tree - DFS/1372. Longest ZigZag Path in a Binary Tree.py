# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, counter, direction):
        if root:
            counter += 1
            self.max_zigzag = max(self.max_zigzag, counter)
            if root.left:
                if direction == 'l':
                    self.dfs(root.left, counter, 'r')
                else:
                    self.dfs(root.left, 0, 'l')
            if root.right:
                if direction == 'r':
                    self.dfs(root.right, counter, 'l')
                else:
                    self.dfs(root.right, 0, 'r')

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_zigzag = 0
        self.dfs(root, 0, 'l')
        self.dfs(root, 0, 'r')
        return self.max_zigzag - 1
