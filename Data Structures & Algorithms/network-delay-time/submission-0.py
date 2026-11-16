from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        node_map = defaultdict(list)

        for ui, vi, ti in times:
            node_map[ui].append((vi, ti))

        dist = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node, time):
            # print(dist)
            if time >= dist[node]:
                return

            dist[node] = time
            for nei, w in node_map[node]:
                dfs(nei, time + w)

        dfs(k, 0)
        # print(dist)
        res = max(dist.values())
        return res if res < float("inf") else -1

        # visited = set()
        # best = 0

        # stack = [(k, 0)]
        # visited = set()
        # while stack:
        #     node = stack.pop()
        #     print("Popped:", node) 

        #     best += node[1]
        #     visited.add(node[0])

        #     if len(visited) == n: return best

        #     directioncost = node_map[node[0]]

        #     for nextnode, cost in directioncost.items():
        #         # if nextnode not in node_map: continue

        #         stack.append((nextnode, cost))

        # return best if len(visited) == n else -1