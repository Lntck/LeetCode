class Solution:
    # Different approach - O(n * (m + k * log(k)))
    # where n = len(s), m = len(words)*len(words[0]), k = len(words)
    # different approach O(n * k * log(k))
    # def findSubstring(self, s: str, words: List[str]) -> List[int]:
    #     n = len(words[0])
    #     k = len(words) * n
    #     if k>len(s): return []
    #     result = []
    #     check_words = sorted(words)
    #     r = k
    #     while r != len(s) + 1:
    #         substr = s[r-k:r]
    #         if sorted([substr[i:i+n] for i in range(0, len(substr), n)]) == check_words:
    #             result.append(r-k)
    #         r += 1
    #     return result

    # Optimized sliding window: O(n * k)
    # where n = len(s), k = len(words)
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        count_words = Counter(words)
        word_len = len(words[0])

        for i in range(word_len):
            freq = count_words.copy()
            start = i
            for j in range(start, len(s) - word_len + 1, word_len):
                curr_word = s[j:j+word_len]
                freq[curr_word] -= 1
                while freq[curr_word] < 0:
                    freq[s[start:start+word_len]] += 1
                    start += word_len
                if freq.total() == 0:
                    result.append(start)
        return result
