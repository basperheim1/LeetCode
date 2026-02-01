class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        minNums = []
        n = len(nums)

        for i in range(1, n): 
            num = nums[i]
            if len(minNums) < 2: 
                minNums.append(num)

            else:
                minNums.sort()
                if num < minNums[1]:
                    minNums[1] = num

        return nums[0] + sum(minNums)
