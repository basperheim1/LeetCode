class Solution:
    def numSub(self, s: str) -> int:

        current_count = 0
        global_count = 0
        for char in s: 
            if char == "1":
                current_count += 1

            else:
                current_count = 0

            global_count += current_count 

        return global_count % (10**9 + 7)
