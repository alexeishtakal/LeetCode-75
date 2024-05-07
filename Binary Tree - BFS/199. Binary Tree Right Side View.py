# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root):
        results = [root.val]
        queue = [root]

        while len(queue) > 0:
            next_level_nodes = []
            for node in queue:
                if node and node.left:
                    next_level_nodes.append(node.left)
                if node and node.right:
                    next_level_nodes.append(node.right)
            if next_level_nodes:
                results.append(next_level_nodes[-1].val)
            queue = next_level_nodes
        return results


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.bfs(root)