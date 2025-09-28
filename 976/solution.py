class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for i in range(n-1, 1, -1):
            long_side = nums[i]
            medium_side = nums[i-1]
            short_side = nums[i-2]

            if long_side < medium_side + short_side: 
                return long_side + medium_side + short_side

        return 0 
