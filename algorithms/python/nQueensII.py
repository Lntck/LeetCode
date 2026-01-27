class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0 

        def backtrack(row: int, cols: set[int], main_diag: set[int], second_diag: set[int]) -> None:
            nonlocal result

            if row == n:
                result += 1
                return

            for i in range(n):
                row, col, main_k, second_k = row, i, (row - i), n - (row + i) - 1
                if col in cols or main_k in main_diag or second_k in second_diag:
                    continue

                cols.add(col)
                main_diag.add(main_k)
                second_diag.add(second_k)

                backtrack(row + 1, cols, main_diag, second_diag)

                cols.remove(col)
                main_diag.remove(main_k)
                second_diag.remove(second_k)

        backtrack(0, set(), set(), set())
        return result
