class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None: return False
        if root.left is None and root.right is None: return root.val == targetSum
        remain_sum = targetSum - root.val
        return self.hasPathSum(root.left, remain_sum) or self.hasPathSum(root.right, remain_sum)
