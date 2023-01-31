# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        seen=set()
        while not current in seen:
            if(current==None):
                return None
            seen.add(current)
            current=current.next
        return current
        