class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        
        def backtrack(x: int, y: int, i: int):
            if len(word) == i: return True
            if not (0 <= x < len(board) and 0 <= y < len(board[0])) or board[x][y] != word[i]:
                return False

            temp, board[x][y] = board[x][y], "*"
            for dx, dy in directions:
                if backtrack(x + dx, y + dy, i+1):
                    board[x][y] = temp
                    return True
            board[x][y] = temp
            return False

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0] and backtrack(x, y, 0):
                    return True
        return False
