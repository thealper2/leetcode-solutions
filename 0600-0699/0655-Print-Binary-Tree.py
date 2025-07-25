from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        if not root:
            return []

        queue = deque([root])
        height = 0

        while queue:
            height += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

        width = (1 << height) - 1
        result = [[''] * width for _ in range(height)]

        queue = deque([
            (root, 0, 0, width - 1)
        ])

        while queue:
            node, level, left, right = queue.popleft()
            mid = (left + right) // 2
            result[level][mid] = str(node.val)

            if node.left:
                queue.append((node.left, level + 1, left, mid - 1))

            if node.right:
                queue.append((node.right, level + 1, mid + 1, right))

        return result

