class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        def index_to_coords(index: int) -> tuple[int, int]:
            return index // m, index % m

        left, right = 0, n*m-1
        while left <= right:
            mid = (left + right) // 2
            x, y = index_to_coords(mid)
            if matrix[x][y] < target:
                left = mid+1
            elif matrix[x][y] > target:
                right = mid-1
            else:
                return True
        return False