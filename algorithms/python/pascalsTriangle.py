class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        for _ in range(1, numRows):
            part_result = [result[-1][i] + result[-1][i+1] for i in range(len(result[-1])-1)]
            result.append([1] + part_result + [1])
        return result
