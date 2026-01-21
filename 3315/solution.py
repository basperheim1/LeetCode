class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums: 
            if num % 2 == 0:
                ans.append(-1)
                continue
            num_bits = list(str(bin(num))[2:])
            n = len(num_bits)
            for i in range(n-1, -1, -1): 
                if num_bits[i] == "0":
                    num_bits[i+1] = "0"
                    break
                if i == 0:
                    num_bits[0] = "0"



            ans.append(int("".join(map(str, num_bits)), 2))

        return ans 
