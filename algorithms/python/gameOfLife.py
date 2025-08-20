class Solution:
    # Сreates a deep copy of the board to preserve original cell states during computation.
    # It counts live neighbors from the copy and applies Game of Life rules to update the original board accordingly.
    def gameOfLife(self, board: List[List[int]]) -> None:
        bd = copy.deepcopy(board)

        row = (-1, -1, -1, 0, 0, 1, 1, 1)
        col = (-1, 0, 1, -1, 1, -1, 0, 1)

        for i in range(len(bd)):
            for j in range(len(bd[0])):
                alive = 0
                for y, x in zip(row, col):
                    if not (0 <= y + i < len(bd) and 0 <= x + j < len(bd[0])):
                        continue
                    alive += bd[y + i][x + j]
                
                if bd[i][j]:
                    if alive < 2:
                        board[i][j] = 0
                    if alive > 3:
                        board[i][j] = 0
                else:
                    if alive == 3:
                        board[i][j] = 1

    # In-place solution uses a two-pass approach with state encoding.
    def gameOfLife(self, board: List[List[int]]) -> None:
        row = (-1, -1, -1, 0, 0, 1, 1, 1)
        col = (-1, 0, 1, -1, 1, -1, 0, 1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                alive = 0
                for y, x in zip(row, col):
                    if not (0 <= y + i < len(board) and 0 <= x + j < len(board[0])):
                        continue
                    if board[y + i][x + j] % 2:
                        alive += 1
                
                if board[i][j]:
                    if 2 <= alive <= 3:
                        board[i][j] += 2
                else:
                    if alive == 3:
                        board[i][j] += 2
        
        # 0 (dead -> dead), 1 (live -> dead), 2 (dead -> live), 3 (live -> live)

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] //= 2
