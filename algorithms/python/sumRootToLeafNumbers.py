class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:        
        def dfs(root: TreeNode | None, curr_sum: int) -> int:
            if not root: return 0

            curr_sum = curr_sum * 10 + root.val
            if not root.left and not root.right: return curr_sum
            return dfs(root.left, curr_sum) + dfs(root.right, curr_sum)
        return dfs(root, 0)
