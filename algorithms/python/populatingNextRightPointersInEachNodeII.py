from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root: return None
        queue = deque([root])

        while queue:
            level_size = len(queue)
            prev_node = None

            for _ in range(level_size):
                curr_node = queue.popleft()

                if prev_node:
                    prev_node.next = curr_node
                prev_node = curr_node

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return root
