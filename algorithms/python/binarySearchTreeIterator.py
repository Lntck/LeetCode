class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode | None):
        self.stack = []
        self._left_push(root)
        
    
    def _left_push(self, root) -> None:
        while root:
            self.stack.append(root)
            root = root.left
    
    def next(self) -> int:
        if not self.hasNext(): raise StopIteration
        node = self.stack.pop()
        self._left_push(node.right)
        return node.val

    def hasNext(self) -> bool:
        return bool(self.stack)
