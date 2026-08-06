class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        rows, cols = len(board), len(board[0])
        directions = ((0, -1), (-1, 0), (0, 1), (1, 0))
        result = []
        trie = {}
        key_word = "@"

        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node[key_word] = word


        def backtrack(x: int, y: int, parent: dict):
            curr_char = board[x][y]
            node = parent[curr_char]

            if key_word in node:
                result.append(node[key_word])
                del node[key_word]

            board[x][y] = "#"
            for dx, dy in directions:
                mx, my = x + dx, y + dy
                if not (0 <= mx < rows and 0 <= my < cols): continue
                if board[mx][my] not in node: continue
                backtrack(mx, my, node)
            board[x][y] = curr_char

            if not node:
                del parent[curr_char]


        for x in range(rows):
            for y in range(cols):
                if board[x][y] in trie:
                    backtrack(x, y, trie)
        return result
