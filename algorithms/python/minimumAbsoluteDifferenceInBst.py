class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode | None) -> int:
        self.min_diff = float("inf")
        self.prev_num = None

        def dfs_inorder(root):
            if not root: return

            dfs_inorder(root.left)

            if self.prev_num is not None:
                self.min_diff = min(root.val - self.prev_num, self.min_diff)
            self.prev_num = root.val

            dfs_inorder(root.right)
        dfs_inorder(root)
        return self.min_diff
