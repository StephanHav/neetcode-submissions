# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return

        root = preorder[0]
        for i in range(len(inorder)):
            if inorder[i] == root:
                left_inorder = inorder[:i]
                right_inorder = inorder[i+1:]

        left_preorder = preorder[1:1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]

        node = TreeNode()
        node.val = root
        
        node.left = self.buildTree(left_preorder, left_inorder)
        node.right = self.buildTree(right_preorder, right_inorder)

        return node







        # Input: preorder = [1,2,3,4], inorder = [2,1,3,4]