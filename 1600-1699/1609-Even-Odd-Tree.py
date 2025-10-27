from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [root]
        level = 0
        while stack:
            level_size = len(stack)
            prev = None
            for i in range(level_size):
                node = stack.pop(0)
                if level % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                else:
                    if node.val % 2 != 0:
                        return False

                if prev is not None:
                    if level % 2 == 0:
                        if node.val <= prev:
                            return False

                    else:
                        if node.val >= prev:
                            return False

                prev = node.val
                if node.left:
                    stack.append(node.left)

                if node.right:
                    stack.append(node.right)

            level += 1

        return True
