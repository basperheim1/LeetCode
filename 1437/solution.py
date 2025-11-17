class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        times_since_k = k

        for num in nums: 
            if num == 1:
                if times_since_k >= k: 
                    times_since_k = 0

                else:
                    return False 
            else: 
                times_since_k += 1

        return True 


