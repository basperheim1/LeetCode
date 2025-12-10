class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        counts_i = dict()
        counts_j_valid = dict()
        zero_count = 0
        total = 0
        for num in nums:
            if num == 0: 
                zero_count += 1
            else:
                if num in counts_i and ((0.5*num) // 1) in counts_j_valid and (num % 2) != 1:
                    total += counts_j_valid[(0.5*num) // 1]

                if num in counts_i:
                    counts_i[num] += 1

                else:
                    counts_i[num] = 1

                if num in counts_j_valid: 
                    if num*2 in counts_i:
                        counts_j_valid[num] += counts_i[num*2]

                else:
                    if num*2 in counts_i: 
                        counts_j_valid[num] = counts_i[num*2]

        if zero_count > 2: 
            total += math.comb(zero_count, 3) 

        return total  % (10**9 + 7)
