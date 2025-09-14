class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in brackets:
                if not stack or stack.pop() != brackets[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack
