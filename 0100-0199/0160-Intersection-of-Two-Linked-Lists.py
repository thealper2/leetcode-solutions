from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes = set()
        
        while headA:
            nodes.add(headA)
            headA = headA.next
        
        while headB:
            if headB in nodes:
                return headB
            headB = headB.next
        
        return None