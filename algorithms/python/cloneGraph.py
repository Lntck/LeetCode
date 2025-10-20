from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = [] if neighbors is None else neighbors


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        if not node: return None

        queue = deque([node])
        orig_to_new = {node: Node(node.val)}

        while queue:
            curr_node = queue.popleft()

            for neighbor in curr_node.neighbors:
                if neighbor not in orig_to_new:
                    queue.append(neighbor)
                    orig_to_new[neighbor] = Node(neighbor.val)
                orig_to_new[curr_node].neighbors.append(orig_to_new[neighbor])
        return orig_to_new[node]
