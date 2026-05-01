# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.appendleft(root)

        res = []
        while len(q) > 0:
            lvl = []
            for _ in range(len(q)):
                root = q.pop()
                if root:
                    lvl.append(root.val)
                    if root.left: 
                        q.appendleft(root.left)
                    if root.right:
                        q.appendleft(root.right)
            res.append(lvl)

        return res

# root=[1,2,3,4,5,6,7]
