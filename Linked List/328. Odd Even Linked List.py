# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = head
        even = head.next
        start_even = even
        while odd and odd.next and odd.next.next:
            odd.next = odd.next.next
            odd = odd.next
            if even.next:
                even.next = even.next.next
                even = even.next
        odd.next = start_even
        return head
