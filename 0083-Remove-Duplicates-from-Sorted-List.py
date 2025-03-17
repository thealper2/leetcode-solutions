# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head

        while current_node:
            while current_node.next and current_node.val == current_node.next.val:
                current_node.next = current_node.next.next

            current_node = current_node.next

        return head
