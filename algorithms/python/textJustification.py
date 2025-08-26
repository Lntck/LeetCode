from typing import List

class Solution:
    def split_number(self, n: int, parts: int) -> List[int]:
        base = n // parts
        remainder = n % parts
        return [base + 1] * remainder + [base] * (parts - remainder)

    def rowJustify(self, words: List[str], maxwidth: int, chars: int, leftJustification=False) -> str:
        if len(words) == 1 or leftJustification:
            line = " ".join(words)
            return line + " " * (maxwidth - len(line))

        spaces = self.split_number(maxwidth - chars, len(words) - 1) + [0]
        return "".join([word + " " * space for word, space in zip(words, spaces)])


    def fullJustify(self, words: List[str], maxwidth: int) -> List[str]:
        result = []
        temp = []
        chars = 0
        for word in words:
            if chars + len(word) + len(temp) <= maxwidth:
                chars += len(word)
                temp.append(word)
            else:
                result.append(self.rowJustify(temp, maxwidth, chars))
                chars = len(word)
                temp = [word]

        if temp:
            result.append(self.rowJustify(temp, maxwidth, chars, leftJustification=True))

        return result
