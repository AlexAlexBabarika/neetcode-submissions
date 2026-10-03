class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        maxx = len(grid[0])
        maxy = len(grid)
        def dfs(x, y):
            if not (0 <= x < maxx): return
            if not (0 <= y < maxy): return
            if grid[y][x] != "1": return
            grid[y][x] = 'x'

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        count = 0
        for v in range(maxy):
            for u in range(maxx):
                if grid[v][u] == "1":
                    dfs(u, v)
                    count += 1
                
        return count
            