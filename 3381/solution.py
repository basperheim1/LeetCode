class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sums = []
        k_total = 0
        for i in range(n-1, -1, -1):
            k_total += nums[i]

            if i <= n - k:
                sums.append(k_total)
                k_total -= nums[i+k-1]


            if i <= n - 2*k:
                if sums[-1-k] > 0:
                    sums[-1] += sums[-1-k]

        return max(sums)



