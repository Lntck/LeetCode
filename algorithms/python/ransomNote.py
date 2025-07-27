class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        for ch in set(ransomNote):
            if magazine.count(ch) < ransomNote.count(ch):
                    return False
        return True
