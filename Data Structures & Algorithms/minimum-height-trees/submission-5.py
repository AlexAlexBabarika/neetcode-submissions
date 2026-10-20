class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edge_cnt = {src: len(neighbors) for src, neighbors in adj.items()}
        leaves = deque([node for node, cnt in edge_cnt.items() if cnt == 1])


        # for src, neighbors in adj.items():
        #     edge_cnt[src] = len(neighbors)
        #     if len(neighbors) == 1:
        #         leaves.append(src)

        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)

        # edge_map = {}

        # for edge in edges:
        #     if edge[0] not in edge_map:
        #         edge_map[edge[0]] = set()
        #         # edge_map[edge[0]].add(edge[1])

        #     if edge[1] not in edge_map:
        #         edge_map[edge[1]] = set()
        #         # edge_map[edge[1]].add(edge[1])

        #     edge_map[edge[0]].add(edge[1])
        #     edge_map[edge[1]].add(edge[0])

        # # print(edge_map)

        # visited = set()
        # def dfs(node, depth=0):
        #     if node in visited: return depth - 1

        #     visited.add(node)
            
        #     max_depth = depth
        #     for n in edge_map[node]:
        #         if n in visited: continue
        #         max_depth = max(dfs(n, depth + 1), max_depth)

        #     return max_depth

        # res = []
        # min_depth = float("inf")
        # for i in range(n):
        #     depth = dfs(i)
        #     visited = set()

        #     if depth < min_depth:
        #         res = []
        #         res.append(i)
        #         min_depth = depth

        #     elif depth == min_depth:
        #         res.append(i)

        # return res

        # # visited_nodes = set()
        # # visited_pairs = []

        # # for i in range(root, curr_edge, depth=0):

        # return [1, 3]





            
        