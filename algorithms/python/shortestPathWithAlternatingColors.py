from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        result = [10**9] * n
        red_edges = defaultdict(list)
        blue_edges = defaultdict(list)

        for fr, to in redEdges:
            red_edges[fr].append(to)
        for fr, to in blueEdges:
            blue_edges[fr].append(to)
        
        visited = set()
        queue = deque([(0, "any", 0)])
        visited.add((0, "any"))

        while queue:
            current, color, cost = queue.popleft()

            result[current] = min(result[current], cost)
            
            if color in ("red", "any"):
                for neighbor in blue_edges[current]:
                    if (neighbor, "blue") not in visited:
                        visited.add((neighbor, "blue"))
                        queue.append((neighbor, "blue", cost + 1))
            if color in ("blue", "any"):
                for neighbor in red_edges[current]:
                    if (neighbor, "red") not in visited:
                        visited.add((neighbor, "red"))
                        queue.append((neighbor, "red", cost + 1))
        
        return [i if i != 10**9 else -1 for i in result]
