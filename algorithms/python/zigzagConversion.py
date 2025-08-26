class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        result = [""] * numRows
        i, direction = 0, 1

        for char in s:
            result[i] += char
            i += direction

            if i == 0 or i + 1 == numRows:
                direction = -direction
        
        return "".join(result)

