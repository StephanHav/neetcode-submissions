# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, min_val, max_val):
            if not node:
                return True # This is the basic case, if we hit a leaf

            if not (min_val < node.val < max_val): 
                return False # we found that the leaves from this root are invalid for a BST.
            
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

        return validate(root, float('-inf'), float('inf'))

        

