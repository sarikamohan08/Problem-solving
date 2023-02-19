# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if(root is None):
            return 0
        lside=self.minDepth(root.left)
        rside=self.minDepth(root.right)
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return 1 + rside
        if root.right is None:
            return 1 + lside
        return(min(lside,rside))+1