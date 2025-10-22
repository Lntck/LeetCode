from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)
        
        def has_cycle(node, history):
            if history[node] == 1:
                return True
            if history[node] == 2:
                return False
            
            history[node] = 1
            for child in graph[node]:
                if has_cycle(child, history):
                    return True
            history[node] = 2
            return False

        history = [0] * numCourses
        for i in range(numCourses):
            if has_cycle(i, history):
                return False
        return True
