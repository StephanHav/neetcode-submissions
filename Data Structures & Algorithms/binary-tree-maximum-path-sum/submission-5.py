# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        if not root.left and not root.right:
            return root.val

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0
            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            max_sum = max(max_sum, (node.val+left), (node.val+right), node.val+left+right)
            return max((node.val+left), (node.val+right))

        dfs(root)

        return max_sum    