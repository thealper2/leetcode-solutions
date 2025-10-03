from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        current_node = head
        while current_node:
            length += 1
            current_node = current_node.next

        result = []
        current_node = head
        min_size = length // k
        extra = length % k

        for i in range(k):
            part_head = current_node
            size = min_size + (1 if extra > 0 else 0)
            extra -= 1 if extra > 0 else 0

            for j in range(size - 1):
                if current_node:
                    current_node = current_node.next

            if current_node:
                next_part = current_node.next
                current_node.next = None
                current_node = next_part

            result.append(part_head)

        return result
