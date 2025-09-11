class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Add all intervals BEFORE newInterval starts
        while i < n and newInterval[0] > intervals[i][-1]:
            result.append(intervals[i])
            i += 1

        # Merge all overlapping intervals with newInterval
        while i < n and newInterval[-1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][-1], newInterval[-1])
            i += 1
        result.append(newInterval)

        # Add all intervals AFTER newInterval ends
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
