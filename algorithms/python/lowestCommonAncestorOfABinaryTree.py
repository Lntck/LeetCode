class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root):
            if not root: return None
            
            left = dfs(root.left)
            right = dfs(root.right)

            if (left and right) or root == p or root == q: return root
            return left or right
        return dfs(root)
    