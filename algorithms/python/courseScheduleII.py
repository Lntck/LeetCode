from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)
        
        def has_cycle(node, history, result):
            if history[node] == 1: return True
            if history[node] == 2: return False

            history[node] = 1
            for child in graph[node]:
                if has_cycle(child, history, result):
                    return True
            result.append(node)
            history[node] = 2
            return False
        
        history = [0] * numCourses
        result = []
        for i in range(numCourses):
            if has_cycle(i, history, result):
                return []
        return result
