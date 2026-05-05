# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        l = 1
        t = head # tail
        while t.next:
            t = t.next
            l += 1
        k = k % l
        if k == 0:
            return head
        t.next = head
        s = l - k #steps
        n = t # new tail
        while s:
            n = n.next
            s -= 1
        nh = n.next #new head
        n.next = None
        return nh