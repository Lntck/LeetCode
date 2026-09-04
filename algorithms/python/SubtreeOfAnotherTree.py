class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def check(sub: TreeNode | None, node: TreeNode | None) -> bool:
            if not sub or not node: return sub is None and node is None
            if sub.val != node.val: return False
            return check(sub.left, node.left) and check(sub.right, node.right)
        
        def dfs(node: TreeNode | None) -> bool:
            if not node: return False

            if node.val == subRoot.val and check(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
