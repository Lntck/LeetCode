class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = [0] * 26

        l = 0
        mx_len = 0
        for r in range(len(s)):
            m[(ord(s[r])) % 26] += 1
    
            while ((r - l) + 1) - max(m) > k:
                m[(ord(s[l])) % 26] -= 1
                l += 1

            mx_len = max(mx_len, r - l + 1)
        return mx_len
