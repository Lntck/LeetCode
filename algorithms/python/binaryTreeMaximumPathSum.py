class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.max_sum = root.val
        def dfs(root):
            if not root: return 0

            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            self.max_sum = max(self.max_sum, left + right + root.val)
            return root.val + max(left, right)
        dfs(root)
        return self.max_sum
