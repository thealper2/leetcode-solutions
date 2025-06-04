from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List:
        if not root:
            return

        queue = [root]        
        nodes = []

        while queue:
            node = queue.pop()
            nodes.append(node.val)
            queue.extend(reversed(node.children))

        return nodes