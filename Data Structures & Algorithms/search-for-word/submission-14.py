class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def find(i, r, c):
            if i == len(word): return True

            if r < 0 or c < 0 or r >= rows or c >= cols or visited[r][c] or board[r][c] != word[i]:
                return False

            visited[r][c] = True
            res = find(i+1, r+1, c) or find(i+1, r-1, c) or find(i+1, r, c+1) or find(i+1, r, c-1)
            visited[r][c] = False
            return res

        for r in range(rows):
            for c in range(cols):
                if find(0, r, c): return True

        return False
            
        