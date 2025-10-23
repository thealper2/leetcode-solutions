from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        self._inorder(root)
        self.index = -1

    def _inorder(self, node):
        if not node:
            return

        self._inorder(node.left)
        self.nodes.append(node.val)
        self._inorder(node.right)

    def next(self) -> int:
        self.index += 1
        return self.nodes[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.nodes)
