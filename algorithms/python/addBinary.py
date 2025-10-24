class Solution:
    # bit by bit addition with carry
    def addBinary(self, a: str, b: str) -> str:
        result = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += 0 if a[i] == "0" else 1
                i -= 1
            if j >= 0:
                carry += 0 if b[j] == "0" else 1
                j -= 1
            result.append(str(carry % 2))
            carry //= 2
        return "".join(reversed(result))
    
    # using built-in conversions (concise but limited by integer size)
    # def addBinary(self, a: str, b: str) -> str:
    #     return bin(int(a, base=2) + int(b, base=2))[2:]
