class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []
    
    def _transfusion(self) -> None:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

    def push(self, x: int) -> None:
        self.input.append(x)
    
    def pop(self) -> int:
        self._transfusion()
        return self.output.pop()

    def peek(self) -> int:
        self._transfusion()
        return self.output[-1]
    
    def empty(self) -> bool:
        return not self.input and not self.output