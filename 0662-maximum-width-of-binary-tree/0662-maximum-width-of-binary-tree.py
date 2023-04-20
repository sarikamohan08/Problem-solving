# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        que = deque([(root,0)])
        while que:
            result = max(result,que[-1][1] - que[0][1] + 1)
            for _ in range(len(que)):
                cur, num = que.popleft()
                if cur.left:
                    que.append((cur.left, num*2))
                if cur.right:
                    que.append((cur.right, num*2 + 1))            
        return result