# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head.next
        a = head
        b = head.next.next
        while b and b.next:
            a = a.next
            b = b.next.next
        a.next = a.next.next
        return head

