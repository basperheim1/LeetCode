class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = nums.copy()

        for i in range(n):
            if nums[i] == 0:
                result[i] = 0

            elif nums[i] > 0:
                result[i] = nums[(i+nums[i]) % n]

            else:
                index = i + nums[i]
                while index < 0:
                    index += n

                result[i] = nums[index]

        return result
        
