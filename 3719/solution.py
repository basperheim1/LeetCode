class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = 0
        for i in range(n):
            odds = set()
            evens = set()
            for j in range(i, n):
                num = nums[j]
                if num not in odds and num not in evens: 
                    if nums[j] % 2 == 1:
                        odds.add(nums[j])

                    else:
                        evens.add(nums[j])

                if len(odds) == len(evens):
                    max_length = max(max_length, j - i + 1)

        return max_length

