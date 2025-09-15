class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        for token in tokens:
            if token in operations:
                b, a = stack.pop(), stack.pop()
                stack.append(operations[token](a, b))
            else:
                stack.append(int(token))
        return stack[-1]
