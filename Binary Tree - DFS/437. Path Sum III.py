# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, current_sum):
        counter = 0
        if root:
            current_sum += root.val
            key = current_sum - self.target_sum
            if key in self.sums:
                counter = self.sums[key]
            else:
                counter = 0
            if current_sum in self.sums:
                self.sums[current_sum] += 1
            else:
                self.sums[current_sum] = 1

            l = self.dfs(root.left, current_sum)
            r = self.dfs(root.right, current_sum)
            counter += l + r
            self.sums[current_sum] -= 1
        return counter

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.target_sum = targetSum
        self.sums = {}
        self.sums[0] = 1
        counter = self.dfs(root, current_sum=0)
        return counter