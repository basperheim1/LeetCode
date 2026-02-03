class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) == 3 or nums[1] < nums[0]:
            return False 
        state = 0
        n = len(nums)
        for i in range(1, n): 
            prev_num = nums[i-1]
            num = nums[i]

            if num == prev_num: 
                return False

            if num > prev_num: 
                if state == 1: 
                    state = 2

            if num < prev_num: 
                if state == 2: 
                    return False 
                if state == 0: 
                    state = 1

        return state == 2
