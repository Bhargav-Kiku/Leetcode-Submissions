# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = []
        nh = head
        while nh:
            a.append(nh.val)
            nh = nh.next
        n = len(a)
        res = 0
        for i in range(n//2):
            res = max(res, a[i] + a[n - 1 - i])
        return res