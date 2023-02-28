# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num=0
        curr=head
        while curr:
            num=(num*10)+curr.val
            curr=curr.next
        return int(str(num),2)