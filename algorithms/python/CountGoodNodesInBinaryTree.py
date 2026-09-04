class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode | None, max_n) -> int:
            if not node: return 0

            if node.val >= max_n:
                return dfs(node.left, node.val) + dfs(node.right, node.val) + 1
            return dfs(node.left, max_n) + dfs(node.right, max_n)
        
        return dfs(root, float("-inf"))
