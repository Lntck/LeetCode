class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(node: TreeNode | None) -> int:
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        if dfs(root) == -1:
            return False
        return True    
