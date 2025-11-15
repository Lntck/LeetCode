class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0: return [1]
        rows = [[1, 1]]
        for i in range(1, rowIndex):
            row = [rows[-1][j] + rows[-1][j+1] for j in range(len(rows[-1])-1)]
            rows[-1] = [1] + row + [1]
        return rows[-1]
