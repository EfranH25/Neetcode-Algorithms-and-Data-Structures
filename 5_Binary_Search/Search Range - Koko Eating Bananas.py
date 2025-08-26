# difficulty: medium
# solution: https://neetcode.io/problems/eating-bananas?list=neetcode150
# my solution

from typing import List
import math

class Solution:
    def check_time(self, piles, k):
        time = 0
        for p in piles:
                time += math.ceil(p/k)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        result = 1


        while L <= R:
            mid = (L + R) // 2

            total_time = self.check_time(piles, mid)

            print(L, mid, R, total_time, total_time <= h)

            if total_time <= h:
                if mid == L:
                    result = mid
                    break
                total_time = self.check_time(piles, mid-1)
                if not total_time <= h:
                    result = mid
                    break
                else:
                    R = mid - 1
            else:
                L = mid + 1

        return result

# improved version
# import math
#
# class Solution:
#     def check_time(self, piles, k):
#         time = 0
#         for p in piles:
#                 time += math.ceil(p/k)
#         return time
#
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         L, R = 1, max(piles)
#         result = 1
#
#
#         while L <= R:
#             mid = (L + R) // 2
#
#             total_time = self.check_time(piles, mid)
#
#             print(L, mid, R, total_time, total_time <= h)
#
#             if total_time <= h:
#                 result = mid
#                 R = mid - 1
#             else:
#                 L = mid + 1
#
#         return result
