# difficulty: easy
# solution: https://neetcode.io/problems/climbing-stairs?list=neetcode150
# my solution - dynamic programming top down

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def climb(n):
            if n <= 1:
                return 1

            if n not in cache:
                val = climb(n - 1) + climb(n - 2)
                cache[n] = val
                return val
            else:
                return cache[n]

        result = climb(n)
        return result


sol = Solution()

sol.climbStairs(5)