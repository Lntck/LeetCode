class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        prev = float("-inf")
        def in_order(node: TreeNode | None) -> bool:
            nonlocal prev

            if not node: return True

            if not in_order(node.left) or prev >= node.val:
                return False
            prev = node.val
            return in_order(node.right)
        return in_order(root)
