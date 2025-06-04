from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        queue = [root]
        seen = set()

        while queue:
            node = queue.pop(0)
            complement = k - node.val
            if complement in seen:
                return True

            seen.add(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return False