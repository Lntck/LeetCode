class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SIZE = 9
        BOX_SIZE = 3

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(SIZE):
            for j in range(SIZE):
                if board[i][j] == ".": continue

                # check row
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])

                # check column
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])

                # check box
                key = (i//BOX_SIZE, j//BOX_SIZE)
                if board[i][j] in boxes[key]:
                    return False
                boxes[key].add(board[i][j])
        return True
