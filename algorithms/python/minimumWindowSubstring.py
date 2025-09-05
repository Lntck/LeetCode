from collections import Counter, defaultdict


class Solution:
    # Sliding window with two pointers and frequency counting.
    # Time complexity is O(n + m), where n = len(s) and m = len(t).
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_freq = Counter(t)
        window_freq = defaultdict(int)
        matched = 0
        min_l, min_len = 0, len(s) + 1
        left = 0

        for right in range(len(s)):
            if s[right] in t_freq:
                window_freq[s[right]] += 1
                if window_freq[s[right]] == t_freq[s[right]]:
                    matched += 1
            
            while matched == len(t_freq):
                if min_len > right-left+1:
                    min_len = right-left+1
                    min_l = left
                
                if s[left] in t_freq:
                    if window_freq[s[left]] == t_freq[s[left]]:
                        matched -= 1
                    window_freq[s[left]] -= 1
                left += 1
        return "" if min_len == len(s) + 1 else s[min_l:min_l+min_len]
