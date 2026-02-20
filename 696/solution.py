class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        prev_zeroes = 0
        prev_ones = 0
        current_ones = 0
        current_zeroes = 0
        for char in s: 
            if char == "0": 
                prev_ones = max(prev_ones, current_ones)
                current_zeroes += 1
                current_ones = 0
                prev_zeroes = 0
                if current_zeroes <= prev_ones: 
                    count += 1

            else:
                prev_zeroes = max(prev_zeroes, current_zeroes)
                current_ones += 1
                current_zeroes = 0
                prev_ones = 0
                if current_ones <= prev_zeroes: 
                    count += 1

        return count 
