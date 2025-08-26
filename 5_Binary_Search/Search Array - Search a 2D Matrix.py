# difficulty: medium
# solution: https://neetcode.io/problems/search-2d-matrix?list=neetcode150
# my solution

from typing import List

class Solution:
    def binary_search(self, arr, target):
        L, R = 0, len(arr) - 1

        while L <= R:
            mid = (L + R) // 2
            if target == arr[mid]:
                return True
            elif target < arr[mid]:
                R = mid - 1
            elif target > arr[mid]:
                L = mid + 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        T, B = 0, len(matrix) - 1

        while T <= B:
            mid = (T + B) // 2
            if target == matrix[mid][0] or target == matrix[mid][-1]:
                return True
            elif matrix[mid][0] < target < matrix[mid][-1]:
                return self.binary_search(matrix[mid], target)
            elif target < matrix[mid][0]:
                B = mid - 1
            elif target > matrix[mid][-1]:
                T = mid + 1

        return False
