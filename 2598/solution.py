class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        times_seen = [0]*value

        for num in nums: 
            if num > 0:
                val = num % value

            elif num < 0: 
                val = (value - ((num*-1) % value)) % value

            else:
                val = 0

            times_seen[val] += 1

        min_seen = min(times_seen)
            

        for i in range(len(times_seen)):
            if times_seen[i] == min_seen: 
                return i + value*min_seen
