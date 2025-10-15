class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:

        n = len(nums)
        increasing_lengths = []

        prev_value = nums[0]
        count = 1
        for i in range(1, n):
                            
            if nums[i] > prev_value: 
                count += 1

            else:
                increasing_lengths.append(count)
                count = 1

            prev_value = nums[i]

        increasing_lengths.append(count)

        m = len(increasing_lengths)

        prev_value = increasing_lengths[0]
        max_value = 0
        for i in range(1, m): 
            max_value = max(max_value, min(prev_value, increasing_lengths[i]))
            prev_value = increasing_lengths[i]

        possible_max = max(increasing_lengths) // 2

        max_value = max(possible_max, max_value)
        return max_value

