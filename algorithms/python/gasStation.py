class Solution:
    # if the total gas is less than the total cost, then it is impossible to complete the circuit.
    # Whenever the current accumulated fuel goes below zero, the journey must restart from the next station.
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        top = 0
        mx_index = 0
        for i in range(len(gas)):
            top = top + gas[i] - cost[i]
            if top < 0:
                top = 0
                mx_index = i + 1
        return mx_index
