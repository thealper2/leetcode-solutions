from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        queue = [root]
        max_depth = 0

        while queue:
            max_depth += 1
            n = len(queue)

            for _ in range(n):
                node = queue.pop(0)
                for child in node.children:
                    queue.append(child)

        return max_depth