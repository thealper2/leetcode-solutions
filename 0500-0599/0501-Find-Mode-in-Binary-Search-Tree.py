from typing import List, Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        count = defaultdict(int)
        max_val = 0
        mode = []

        while queue:
            node = queue.pop(0)
            count[node.val] += 1
            if count[node.val] > max_val:
                max_val = count[node.val]

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        for k, v in count.items():
            if v == max_val:
                mode.append(k)

        return mode