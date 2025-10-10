class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        def flat(root: TreeNode | None) -> TreeNode | None:
            if not root: return None

            last_right = flat(root.right)
            last_left = flat(root.left)

            if root.left:
                last_left.right = root.right
                root.right = root.left
                root.left = None
            
            return last_right or last_left or root
        flat(root)
    