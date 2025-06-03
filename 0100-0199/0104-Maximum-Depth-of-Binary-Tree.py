from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        
        queue = [root]
        max_depth = 0

        while queue:
            max_depth += 1
            n = len(queue)

            for _ in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return max_depth