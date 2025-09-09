class Solution:
    # Time complexity O(n*m), Space complexity O(n+m)
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     rows, cols = [False] * len(matrix), [False] * len(matrix[0])

    #     for y in range(len(matrix)):
    #         for x in range(len(matrix[0])):
    #             if matrix[y][x] == 0:
    #                 rows[y] = True
    #                 cols[x] = True
        
    #     for y in range(len(matrix)):
    #         for x in range(len(matrix[0])):
    #             if rows[y] or cols[x]:
    #                 matrix[y][x] = 0

    # In-place Solution, Time complexity O(n*m), Space complexity O(1)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        row_has_zero = any(matrix[0][i] == 0 for i in range(m))
        col_has_zero = any(matrix[i][0] == 0 for i in range(n))

        for y in range(n):
            for x in range(m):
                if matrix[y][x] == 0:
                    matrix[y][0] = 0
                    matrix[0][x] = 0

        for y in range(1, n):
            for x in range(1, m):
                if matrix[y][0] == 0 or matrix[0][x] == 0:
                    matrix[y][x] = 0
        
        if col_has_zero:
            for y in range(n):
                matrix[y][0] = 0
        if row_has_zero:
            for x in range(m):
                matrix[0][x] = 0
