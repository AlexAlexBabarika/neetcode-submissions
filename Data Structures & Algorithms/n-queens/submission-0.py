class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag_pos = set()
        diag_neg = set()

        board = [[False] * n for _ in range(n)]

        result = []

        def backtrack(r):
            if r == n:
                rows = []
                for row in board:
                    colstr = ""
                    for col in row:
                        colstr += 'Q' if col else '.'
                    rows.append(colstr)
                result.append(rows)
                return

            for c in range(n):
                if c in cols or (r + c) in diag_pos or (r - c) in diag_neg:
                    continue

                cols.add(c)
                diag_pos.add(r + c)
                diag_neg.add(r - c)
                board[r][c] = True

                backtrack(r + 1)

                cols.remove(c)
                diag_pos.remove(r + c)
                diag_neg.remove(r - c)
                board[r][c] = False

        backtrack(0)
        print(result)

        return result