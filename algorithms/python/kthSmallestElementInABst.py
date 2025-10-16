class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.result = None
        self.counter = 0

        def dfs(node):
            if not node or self.result is not None: return

            dfs(node.left)
            if self.result is not None: return

            self.counter += 1
            if self.counter == k:
                self.result = node.val
                return
            
            dfs(node.right)
        dfs(root)
        return self.result
