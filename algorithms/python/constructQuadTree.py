class Node:
    def __init__(self, val: bool, isLeaf: bool, topLeft: Node | None = None, topRight: Node | None = None, bottomLeft: Node | None = None, bottomRight: Node | None = None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        def divide_conquer(left: int, right: int, top: int, bottom: int) -> Node:
            if left == right and top == bottom:
                return Node(bool(grid[top][left]), True)

            topLeft = divide_conquer(left, (right + left) // 2, top, (top + bottom) // 2)
            topRight = divide_conquer((right + left) // 2 + 1, right, top, (top + bottom) // 2)
            bottomLeft = divide_conquer(left, (right + left) // 2, (top + bottom) // 2 + 1, bottom)
            bottomRight = divide_conquer((right + left) // 2 + 1, right, (top + bottom) // 2 + 1, bottom)
            
            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf) and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(topLeft.val, True)
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        return divide_conquer(0, len(grid) - 1, 0, len(grid) - 1)
