# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
                tmp=head
                prev=head
                while tmp and tmp.next:
                    tmp=tmp.next.next
                    prev=prev.next

                return prev