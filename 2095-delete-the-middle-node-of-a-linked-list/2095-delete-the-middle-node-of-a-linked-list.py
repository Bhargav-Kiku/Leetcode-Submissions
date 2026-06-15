# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        nh = head
        while nh:
            n += 1
            nh = nh.next
        if n == 1:
            return None
        n //= 2
        n -= 1
        nh = head
        while n:
            n -= 1
            nh = nh.next
        nh.next = nh.next.next
        return head