class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        val_to_index = {val: index for index, val in enumerate(inorder)}

        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end: return None
            root = TreeNode(preorder[pre_start])
            root_index = val_to_index[root.val]

            left_size = root_index - in_start

            root.left = build(pre_start + 1, pre_start + left_size + 1, in_start, root_index - 1)
            root.right = build(pre_start + 1 + left_size, pre_end, root_index + 1, in_end)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
