from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1/value))

        def bfs(start: str, end: str) -> float:
            if start not in graph or end not in graph: return -1
            if start == end: return 1

            queue = deque([(start, 1)])
            visited = set()

            while queue:
                node, weight = queue.popleft()
                visited.add(node)
                for dest, dest_weight in graph[node]:
                    if dest in visited: continue
                    if end == dest:
                        return weight * dest_weight
                    queue.append((dest, weight * dest_weight))
            return -1

        return [bfs(start, end) for start, end in queries]
