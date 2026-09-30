"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        ancestor = None
        def clone(node):
            nonlocal clones
            nonlocal ancestor

            if node is None: 
                return 

            new_node = Node(node.val)
            clones[node.val] = new_node

            if ancestor is None: 
                ancestor = new_node 

            for neighbor in node.neighbors:
                if neighbor.val not in clones:
                    clone(neighbor)

                new_node.neighbors.append(clones[neighbor.val])

        clone(node)
        return ancestor


        