class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        for ch in s1:
            count_s1[ch] = count_s1.get(ch, 0) + 1
        
        count_s2 = {}
        l = 0
        for r in range(len(s2)):
            count_s2[s2[r]] = count_s2.get(s2[r], 0) + 1

            while count_s1.get(s2[r], 0) < count_s2.get(s2[r], 0):
                if count_s2[s2[l]] == 1:
                    del count_s2[s2[l]]
                else:
                    count_s2[s2[l]] -= 1
                l += 1

            if count_s1 == count_s2:
                return True
        return False
