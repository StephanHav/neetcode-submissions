# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        hmap = {}
        for i, num in enumerate(inorder):
            hmap[num] = hmap.get(num, i)
        
        pre_idx = 0

        def helper(left_bound, right_bound):
            nonlocal pre_idx

            if left_bound > right_bound:
                return None

            root = preorder[pre_idx]
            pre_idx += 1
            mid = hmap[root]
            
            node = TreeNode(root)

            node.left = helper(left_bound, mid - 1)
            node.right = helper(mid + 1, right_bound)
            return node

        return helper(pre_idx, len(preorder) - 1)










        # Input: preorder = [1,2,3,4], inorder = [2,1,3,4]