from collections import deque


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        def remove_zeros(row, col):
            if board[row][col] != "O": return

            queue = deque([(row, col)])
            board[row][col] = "#"

            while queue:
                row, col = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    x = row + dx
                    y = col + dy
                    if (0 <= x < len(board) and 0 <= y < len(board[0])):
                        if board[x][y] == "O":
                            board[x][y] = "#"
                            queue.append((x, y))
        
        for col in range(len(board[0])):
            remove_zeros(0, col)
            remove_zeros(len(board)-1, col)
        for row in range(1, len(board)-1):
            remove_zeros(row, 0)
            remove_zeros(row, len(board[0])-1)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "#":
                    board[row][col] = "O"
