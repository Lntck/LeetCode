class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        map_s_to_t = {}
        set_t = set()
        
        for i in range(len(s)):
            if s[i] in map_s_to_t:
                if map_s_to_t[s[i]] != t[i]:
                    return False
            else:
                if t[i] in set_t:
                    return False
                map_s_to_t[s[i]] = t[i]
                set_t.add(t[i])
        return True
