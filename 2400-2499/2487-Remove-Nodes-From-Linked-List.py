from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current:
            while stack and stack[-1].val < current.val:
                stack.pop()

            stack.append(current)
            current = current.next
        
        dummy = ListNode(0)
        prev = dummy
        for node in stack:
            prev.next = node
            prev = node

        prev.next = None
        return dummy.next
