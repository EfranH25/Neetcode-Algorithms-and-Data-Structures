# difficulty: easy
# solution: https://neetcode.io/problems/reverse-a-linked-list?list=neetcode150
# my solution

from typing import List

# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output = []
        # output.append(pairs.copy())
        for i in range(0, len(pairs)):
            j = i - 1

            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                pairs[j + 1], pairs[j] = pairs[j], pairs[j + 1]
                j -= 1
            output.append(pairs[:])

        return output