class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        mx = 0

        def func(root: TreeNode | None) -> int:
            nonlocal mx
            if not root: return 0

            left = func(root.left)
            right = func(root.right)
            mx = max(mx, right + left)
            return max(left, right) + 1
        func(root)
        return mx
