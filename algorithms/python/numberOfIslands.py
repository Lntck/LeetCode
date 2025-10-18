class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def is_valid(row: int, col: int) -> bool:
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def remove_island(row: int, col: int) -> None:
            if not is_valid(row, col): return

            if grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"
            
            remove_island(row+1, col)
            remove_island(row-1, col)
            remove_island(row, col+1)
            remove_island(row, col-1)
                
        c = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    c += 1
                    remove_island(row, col)
        return c
