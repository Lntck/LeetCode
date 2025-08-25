class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyToResult = {}

        for word in strs:
            key = tuple(sorted(word))
            if key in keyToResult:
                keyToResult[key].append(word)
            else:
                keyToResult[key] = [word]

        return list(keyToResult.values())
