from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if startGene == endGene: return 0

        choices = ("A", "C", "G", "T")
        queue = deque([(startGene, 0)])
        bank = set(bank)
        visited = set()
        while queue:
            gene, mutations = queue.popleft()

            if gene == endGene:
                return mutations

            for i in range(len(gene)):
                for step in choices:
                    newGene = gene[:i] + step + gene[i+1:]
                    if newGene in bank and newGene not in visited:
                            visited.add(newGene)
                            queue.append((newGene, mutations + 1))
        return -1
