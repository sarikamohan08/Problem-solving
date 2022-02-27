"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        # initialize the first child of the level 
        firstChild = root
        
        while firstChild:
            actual = firstChild
            firstChild = firstChild.left
            
            # while the actual level has siblings, we keep looping, if not we finish this while and we move into the next level
            while actual:
                if actual.left:
                    # connect left child with right child of the same node
                    actual.left.next = actual.right
                    # if the next sibling exists and it has a left child, we connect the actual right child with the next left child
                    if actual.next:
                        actual.right.next = actual.next.left
                else:
                    break
                # update the actual node with the next sibling (at the same level)
                # if the next sibling is Null, this loops ends and we go to the next level
                actual = actual.next
        
        return root