# difficulty: easy
# solution: https://neetcode.io/problems/k-closest-points-to-origin?list=neetcode150
# my solution

from typing import List, Optional
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_list = []

        def dist(x1,y1,x2,y2):
            a = (x1-x2)**2
            b = (y1-y2)**2
            return math.sqrt(a + b)

        for p in points:
            dist_val = dist(0,0, p[0], p[1])
            heapq.heappush(dist_list, (-dist_val, p))
            if len(dist_list) > k:
                heapq.heappop(dist_list)

        result = []
        for i in range(k):
            result.append(heapq.heappop(dist_list)[1])

        return result
