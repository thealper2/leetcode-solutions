from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        max_depth = 0
        deepest_sum = 0

        while queue:
            node, depth = queue.popleft()

            if depth > max_depth:
                max_depth = depth
                deepest_sum = 0

            if not node.left and not node.right and depth == max_depth:
                deepest_sum += node.val

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))

        return deepest_sum