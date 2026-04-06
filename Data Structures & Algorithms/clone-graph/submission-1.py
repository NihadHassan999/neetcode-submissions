'''
-> cover edge case if input is empty
-> Create hashmap to store cloned adjacent list graph
-> first clone current node and recursively clone neighbours
'''


# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Hash map to store cloned nodes
        cloned_nodes = {}

        # Recursive DFS function
        def dfs(curr_node):
            # If already cloned, return the clone
            if curr_node in cloned_nodes:
                return cloned_nodes[curr_node]

            # Clone the node
            clone = Node(curr_node.val)
            cloned_nodes[curr_node] = clone

            # Recursively clone all neighbors
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)


'''
Time compplexity : O(V + E)
Space complexity : O(V)
'''
















        