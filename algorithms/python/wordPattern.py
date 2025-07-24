class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str_to_patt = {}
        s = s.split()

        if len(s) != len(pattern) or len(set(s)) != len(set(pattern)):
            return False
        
        for i in range(len(pattern)):
            if s[i] in str_to_patt and str_to_patt[s[i]] != pattern[i]:
                return False
            else:
                str_to_patt[s[i]] = pattern[i]
        return True
