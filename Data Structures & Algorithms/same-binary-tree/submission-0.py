# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        #we already know that both aren't None
        if not p or not q:
            return False

        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)


        # p=[1,2,3]
        # q=[1,2,3]

        