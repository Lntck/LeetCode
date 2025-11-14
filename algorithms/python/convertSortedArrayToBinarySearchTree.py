class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        
        def create_tree(start: int, end: int) -> TreeNode | None:
            if start > end: return None
            mid = (end + start) // 2
            node = TreeNode(nums[mid])
            node.left = create_tree(start, mid-1)
            node.right = create_tree(mid+1, end)
            return node

        return create_tree(0, len(nums)-1)