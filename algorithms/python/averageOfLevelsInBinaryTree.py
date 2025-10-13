from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                curr_node = queue.popleft()
                level_sum += curr_node.val

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            result.append(level_sum / level_size)
        return result
