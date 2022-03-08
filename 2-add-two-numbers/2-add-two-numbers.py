# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        tail = None
        sum = 0
        while(l1 or l2 or sum > 0):
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            lNode = ListNode(sum % 10)
            if head is None:
                tail = head = lNode
            else:    
                tail.next = lNode
                tail = lNode
            sum = sum > 9
        return head