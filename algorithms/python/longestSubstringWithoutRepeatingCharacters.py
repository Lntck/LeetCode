class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        in_window = {}
        l, longest_sub = 0, 0

        for r, ch in enumerate(s):
            if ch in in_window:
                l = max(l, in_window[ch] + 1)

            in_window[ch] = r
            longest_sub = max(longest_sub, r-l+1)
        return longest_sub
