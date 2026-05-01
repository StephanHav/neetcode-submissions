"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hmap = {}
        
        def dfs(node):
            if not node in hmap:
                copy = Node(node.val)
                hmap[node] = copy
                for neighbor in node.neighbors:
                    clone = dfs(neighbor)
                    hmap[node].neighbors.append(clone)
            return hmap[node]
        
        return dfs(node)