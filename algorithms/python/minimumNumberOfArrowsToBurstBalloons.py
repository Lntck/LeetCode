class Solution:
    # code from leetcode #56 simple replaced with min
    # def findMinArrowShots(self, points: List[List[int]]) -> int:
    #     points.sort(key=lambda x: x[0])
    #     result = [points[0]]
    #     for i in range(1, len(points)):
    #         if result[-1][-1] >= points[i][0]:
    #             result[-1][-1] = min(result[-1][-1], points[i][-1])
    #         else:
    #             result.append(points[i])
    #     return len(result)

    # Optimized solution
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        result = 1
        last = points[0][-1]
        for start, end in points[1:]:
            if start > last:
                last = end
                result += 1
        return result
