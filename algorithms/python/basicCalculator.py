class Solution:
    # Time complexity - O(n), Space Complexity - O(d), d - max depth of parentheses
    def calculate(self, s: str) -> int:
        cur = 0
        res = 0
        sign = 1
        stack = []

        for ch in s:
            if ch == " ": continue

            if ch.isdigit():
                cur = cur * 10 + int(ch)
            else:
                res += cur * sign
                cur = 0
                sign = 1 if ch == "+" else (-1 if ch == "-" else sign)

                if ch == "(":
                    stack.append(res)
                    stack.append(sign)
                    cur = 0
                    sign = 1
                    res = 0
                elif ch == ")":
                    res *= stack.pop()
                    res += stack.pop()
        return res + cur * sign
