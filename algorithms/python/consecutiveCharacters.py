class Solution:
    def maxPower(self, s: str) -> int:
        max_power, power = 1, 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                power += 1
                max_power = max(max_power, power)
            else:
                power = 1
        return max_power