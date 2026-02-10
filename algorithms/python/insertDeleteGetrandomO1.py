import random


class RandomizedSet:
    def __init__(self):
        self.randomized_set = []
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.randomized_set.append(val)
        self.hashmap[val] = len(self.randomized_set) - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.hashmap: return False

        index = self.hashmap[val]
        
        self.hashmap[self.randomized_set[-1]] = index
        del self.hashmap[val]

        self.randomized_set[index] = self.randomized_set[-1]

        self.randomized_set.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.randomized_set)
