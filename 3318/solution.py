class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        arr = []
        for i in range(len(nums) - k + 1):
            num_sub_arr = nums[i:i+k]

            counts = dict()
            for num in num_sub_arr:
                if num in counts: 
                    counts[num] += 1

                else:
                    counts[num] = 1

            keys_sorted = sorted(counts, key=lambda k: (counts[k], k))
            keys_sorted.reverse()
            print(keys_sorted)

            arr.append(0)
            for j in range(min(x, len(keys_sorted))):
                arr[i] += keys_sorted[j]*counts[keys_sorted[j]]

        return arr




            
