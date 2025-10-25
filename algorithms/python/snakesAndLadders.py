from collections import deque


class Solution:
    def convert_coords(self, n: int, step: int) -> tuple[int, int]:
        quot, rem = divmod(step - 1, n)
        row = n - 1 - quot
        if (n - 1 - row) % 2 == 0:
            return row, rem
        return row, n - 1 - rem

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        queue = deque([(1, 0)])
        visited = [False] * (n * n + 1)
        while queue:
            position, rolls = queue.popleft()

            if position == n * n:
                return rolls

            for next_step in range(position + 1, min(position + 6, n * n) + 1):
                row, col = self.convert_coords(n, next_step)
                if not visited[next_step]:
                    if board[row][col] != -1:
                        queue.append((board[row][col], rolls + 1))
                    else:
                        queue.append((next_step, rolls + 1))
                    visited[next_step] = rolls + 1
        return -1
