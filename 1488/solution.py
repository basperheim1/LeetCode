from typing import List

class Solution: 
    def avoidFlood(self, rains: List[int]):
        n = len(rains)
        recent_lake_flood = [-1 for _ in range(n)]