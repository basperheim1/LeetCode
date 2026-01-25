class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        n = len(nums)
        nums.sort()

        lp = 0
        rp = k - 1
        minimum = 1000000000

        while rp != n: 
            current_min = nums[rp] - nums[lp]
            minimum = min(minimum, current_min)

            lp += 1
            rp += 1

        return minimum
