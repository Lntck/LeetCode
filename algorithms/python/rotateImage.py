class Solution:
    # In-place solution that rotates the matrix 90 degrees (clockwise)
    # Transpose -> reverse rows
    def rotate(self, matrix: List[List[int]]):
        n = len(matrix)

        for y in range(n):
            for x in range(y+1):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
        
        for y in range(n):
            for x in range(n // 2):
                matrix[y][x], matrix[y][n-x-1] = matrix[y][n-x-1], matrix[y][x]
