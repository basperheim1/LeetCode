class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        n = len(nums)

        for i in range(0, n - 2*k + 1):
            print(i)
            prev_val = nums[i]
            count = 1

            found = True 
            for j in range(i+1, i + 2*k):

                if count != k:
                    if nums[j] <= prev_val: 
                        found = False 
                        break

                count += 1
                prev_val = nums[j]

            if found: 
                return True

        return False

