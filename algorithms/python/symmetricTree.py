class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def is_mirror(p1: TreeNode | None, p2: TreeNode | None) -> bool:
            if p1 is None and p2 is None: return True
            if p1 is None or p2 is None: return False
            return p1.val == p2.val and is_mirror(p1.left, p2.right) and is_mirror(p1.right, p2.left)
        return is_mirror(root.left, root.right)
