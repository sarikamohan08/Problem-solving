# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import sys
        sys.setrecursionlimit(10**6)
        current=head
        while(current and current.next):
                current.val,current.next.val=current.next.val,current.val
                current=current.next.next
        return head
            