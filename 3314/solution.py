class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums: 
            if num % 2 == 0: 
                ans.append(-1)
                continue 

            for i in range(1, 1000):
                if i | (i + 1) == num: 
                    ans.append(i)
                    break

        return ans 
