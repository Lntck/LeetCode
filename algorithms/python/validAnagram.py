class Solution:
    # Time complexity: O(n), Space complexity: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sl1 = {}
        for ch in s:
            sl1[ch] = sl1.get(ch, 0) + 1
        
        for ch in t:
            if sl1.get(ch, 0) == 0:
                return False
            sl1[ch] -= 1
        return True
