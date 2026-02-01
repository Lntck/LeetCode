from collections import deque


class Solution:
    def finalString(self, s: str) -> str:
        queue = deque([])
        switch = True
        for ch in s:
            if ch == "i": switch = not switch
            else: queue.append(ch) if switch else queue.appendleft(ch)
        result = "".join(queue)
        return result if switch else result[::-1]
