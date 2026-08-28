class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        count, mx = 0, 0
        for pos, spd in cars:
            if (target - pos) / spd > mx:
                mx = (target - pos) / spd
                count += 1
        return count
