class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        val_to_index = {val: index for index, val in enumerate(inorder)}

        def build(post_start: int, post_end: int, in_start: int, in_end: int) -> TreeNode | None:
            if post_start > post_end or in_start > in_end: return None
            root = TreeNode(postorder[post_end])
            root_index = val_to_index[root.val]

            left_size = root_index - in_start

            root.left = build(post_start, post_start + left_size - 1, in_start, root_index - 1)
            root.right = build(post_start + left_size, post_end - 1, root_index + 1, in_end)
            return root

        return build(0, len(postorder) - 1, 0, len(inorder) - 1)
