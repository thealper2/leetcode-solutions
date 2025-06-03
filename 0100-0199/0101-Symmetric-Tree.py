from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    def symmetric(node1, node2):
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False
        
        if node1.val != node2.val:
            return False
        
        return symmetric(node1.left, node2.right) and symmetric(node1.right, node2.left)

    return symmetric(root.left, root.right)