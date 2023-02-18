# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if(root is None):
            return -1
        lside=self.height(root.left)
        rside=self.height(root.right)
        if(lside>rside):
            return lside+1
        else:
            return rside+1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(root is None):
            return True
        lh=self.height(root.left)
        rh=self.height(root.right)
        
        if(abs(lh-rh)>1):
            return False
        lside=self.isBalanced(root.left)
        rside=self.isBalanced(root.right)
        
        if(lside==True and rside==True):
            return True
        else:
            return False