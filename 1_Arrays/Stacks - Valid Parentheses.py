# difficulty: easy
# Solution: https://neetcode.io/problems/validate-parentheses?list=neetcode150
# my solution
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        options = {
            '[': ']',
            '(': ')',
            '{': '}'
        }

        stack = deque([])
        for letter in s:
            print(stack, letter)
            if letter in options.keys():
                stack.append(letter)
            elif stack:
                top = stack.pop()
                if options[top] != letter:
                    return False
            else: return False

        return False if stack else True
