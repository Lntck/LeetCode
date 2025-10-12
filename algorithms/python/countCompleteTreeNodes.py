class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # count nodes in complete binary tree in better than O(n)
    # O(log^2 n) solution
    def countNodes(self, root: TreeNode | None) -> int:
        if not root: return 0
        
        # calculate the height
        height = 0
        curr = root
        while curr:
            height += 1
            curr = curr.left
        
        # maximum possible nodes at the last level
        max_nodes_last_level = (1 << (height - 1))

        def exists(root: TreeNode, index: int,  height: int) -> bool:
            left, right = 0, (1 << (height - 1)) - 1
            
            for _ in range(height-1):
                mid = (left + right) // 2
                if index <= mid:
                    root = root.left
                    right = mid
                else:
                    root = root.right
                    left = mid
                if not root: return False
            return True

        left, right = 0, max_nodes_last_level - 1
        while left <= right:
            mid = (left + right) // 2
            if exists(root, mid, height):
                left = mid + 1
            else:
                right = mid - 1

        # max_nodes_last_level already represents the count we need
        # nodes_above_last_level = max_nodes_last_level - 1
        # nodes_last_level = right + 1
        return max_nodes_last_level + right
