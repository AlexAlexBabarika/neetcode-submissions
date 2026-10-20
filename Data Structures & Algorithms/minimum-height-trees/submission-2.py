class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges: return [0]

        edge_map = {}

        for edge in edges:
            if edge[0] not in edge_map:
                edge_map[edge[0]] = set()
                # edge_map[edge[0]].add(edge[1])

            if edge[1] not in edge_map:
                edge_map[edge[1]] = set()
                # edge_map[edge[1]].add(edge[1])

            edge_map[edge[0]].add(edge[1])
            edge_map[edge[1]].add(edge[0])

        # print(edge_map)

        visited = set()
        def dfs(node, depth=0):
            if node in visited: return depth - 1

            visited.add(node)
            
            max_depth = depth
            for n in edge_map[node]:
                if n in visited: continue
                max_depth = max(dfs(n, depth + 1), max_depth)

            return max_depth

        res = []
        min_depth = float("inf")
        for i in range(n):
            depth = dfs(i)
            visited = set()

            if depth < min_depth:
                res = []
                res.append(i)
                min_depth = depth

            elif depth == min_depth:
                res.append(i)

        return res

        # visited_nodes = set()
        # visited_pairs = []

        # for i in range(root, curr_edge, depth=0):

        return [1, 3]





            
        