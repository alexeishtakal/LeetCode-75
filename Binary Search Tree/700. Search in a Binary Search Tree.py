# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, val):
        if root:
            if root.val == val:
                return root
            result = None
            if root.left:
                result = self.dfs(root.left, val)

            if root.right:
                r = self.dfs(root.right, val)
                if r:
                    result = r
            return result
        return None

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.dfs(root, val)