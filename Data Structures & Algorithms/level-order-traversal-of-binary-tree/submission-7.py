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
        q.append(root)

        res = []
        while len(q) > 0:
            lvl = []
            for _ in range(len(q)):
                root = q.popleft()
                if root:
                    lvl.append(root.val)
                    if root.left: 
                        q.append(root.left)
                    if root.right:
                        q.append(root.right)
            res.append(lvl)

        return res

# root=[1,2,3,4,5,6,7]
