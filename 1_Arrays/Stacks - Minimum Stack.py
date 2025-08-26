
# difficulty: medium
# Solution: https://neetcode.io/problems/minimum-stack?list=neetcode150
# my solution
class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.smallest = [] #tracking the minimum value during each push

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.smallest[-1] if self.smallest else val)
        self.smallest.append(val)
        self.size += 1



    def pop(self) -> None:
        top = None
        if self.size > 0:
            self.stack.pop()
            self.smallest.pop()


    def top(self) -> int:
        top = None
        if self.size > 0:
            top = self.stack[-1]
        return top

    def getMin(self) -> int:
        return self.smallest[-1]

