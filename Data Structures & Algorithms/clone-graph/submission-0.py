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
                print("Node is none")
                return 

            new_node = Node(node.val)
            clones[node.val] = new_node

            if ancestor is None: 
                print("Set new ancestor: ", new_node.val)
                ancestor = new_node 

            for neighbor in node.neighbors:
                if neighbor.val in clones:
                    print(neighbor.val, " is in clones")

                else:
                    print("clone: ", neighbor.val)
                    clone(neighbor)

                new_node.neighbors.append(clones[neighbor.val])

        clone(node)
        return ancestor


        