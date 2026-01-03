class Solution:
    def numOfWays(self, n: int) -> int:
        duplicate_count = 6
        single_count = 6
        for i in range(1, n):
            new_duplicate_count = duplicate_count*3 + single_count*2
            new_single_count = duplicate_count*2 + single_count*2

            duplicate_count = new_duplicate_count
            single_count = new_single_count

        return (single_count + duplicate_count) % (10**9 + 7)
