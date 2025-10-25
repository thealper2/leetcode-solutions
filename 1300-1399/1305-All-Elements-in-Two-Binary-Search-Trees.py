from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        result = []
        def inorder(node, result):
            if not node:
                return

            inorder(node.left, result)
            result.append(node.val)
            inorder(node.right, result)

        inorder(root1, result)
        inorder(root2, result)
        return sorted(result)
