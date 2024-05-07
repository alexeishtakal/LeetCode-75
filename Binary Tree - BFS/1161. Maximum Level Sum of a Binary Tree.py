# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        max_value = root.val
        level = 1
        max_level = 1

        while len(queue) > 0:
            level_sum = 0
            next_level_nodes = []
            for node in queue:

                level_sum += node.val

                if node and node.left:
                    next_level_nodes.append(node.left)
                if node and node.right:
                    next_level_nodes.append(node.right)

            if level_sum > max_value:
                max_value = level_sum
                max_level = level
            queue = next_level_nodes
            level += 1

        return max_level



