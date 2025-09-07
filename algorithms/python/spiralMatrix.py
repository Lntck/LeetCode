class Solution:
    # Recursive solution
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     return list(matrix[0]) + self.spiralOrder(list(zip(*matrix[1:]))[::-1]) if matrix else []
    # take the first row + rotate the rest of the matrix counter-clockwise and repeat


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left_border, up_border, right_border, down_border = 0, 0, len(matrix[0]), len(matrix)
        result = []

        while (left_border < right_border and up_border < down_border):
            for i in range(left_border, right_border):
                result.append(matrix[up_border][i])
            up_border += 1

            for i in range(up_border, down_border):
                result.append(matrix[i][right_border-1])
            right_border -= 1
            
            if not (left_border < right_border and up_border < down_border):
                return result

            for i in range(right_border-1, left_border-1, -1):
                result.append(matrix[down_border-1][i])
            down_border -= 1

            for i in range(down_border-1, up_border-1, -1):
                result.append(matrix[i][left_border])
            left_border += 1
        return result
